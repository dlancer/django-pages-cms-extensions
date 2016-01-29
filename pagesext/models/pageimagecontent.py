"""Implements page image extended content model"""

from __future__ import unicode_literals

import os
import uuid
import hashlib
import base64

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete
from django.dispatch import receiver

from image_cropping import ImageCropField
from image_cropping import ImageRatioField

from taggit.managers import TaggableManager

from pages.conf import settings
from pages.models.pagebasecontent import PageBaseContent
from pagesext.storage import PageExtFileSystemStorage
from pagesext.conf import settings as ext_settings

if settings.PAGES_PAGE_USE_EXT_CONTENT_TYPES:

    image_file_storage = PageExtFileSystemStorage()

    def make_image_upload_path(instance, filename, prefix=False):
        """Generate upload path and filename for image"""

        # store original filename
        instance.filename = filename
        ext = os.path.splitext(filename)[1].strip('.').lower()

        # always generate unique path, for security and file system balancing reasons
        file_uuid = uuid.uuid4().hex

        # generate short sha1 based hash
        name_sha = hashlib.sha1(file_uuid).digest()
        name_hash = base64.urlsafe_b64encode(name_sha[:9]).decode('utf-8')

        if ext_settings.PAGES_EXT_IMAGE_USE_ORIGINAL_FILENAME:
            name = image_file_storage.get_available_name(os.path.splitext(filename)[0])
        else:
            name = name_hash

        return u'{path}/{sub0}/{sub1}/{sub2}/{name}.{ext}'.format(
                path=settings.PAGES_EXT_IMAGE_DIR,
                sub0=file_uuid[0:2],
                sub1=file_uuid[7:9],
                sub2=file_uuid[12:14],
                name=name,
                ext=ext
        )

    class PageImageContent(PageBaseContent):
        image = ImageCropField(blank=True, null=True, upload_to=make_image_upload_path, storage=image_file_storage)
        cropping = ImageRatioField('image', '{0:>s}x{1:>s}'.format(
                str(settings.PAGES_EXT_IMAGE_WIDTH_MAX), str(settings.PAGES_EXT_IMAGE_HEIGHT_MAX)), allow_fullsize=True)
        title = models.CharField(max_length=250, blank=True)
        tags = TaggableManager()
        objects = models.Manager()

        def update_fields(self, change):
            if not change:
                self.type = 'image'
                self.is_extended = True

        def image_cropping_link(self):
            """Return image cropping link"""
            change_url = reverse('admin:pagesext_pageimagecontent_change', args=(self.id,))
            return '<a href="{0:>s}" onclick="return showAddAnotherPopup(this);">{1:>s}</a>'.format(change_url, _('CROP'))

        image_cropping_link.short_description = _('Cropping')
        image_cropping_link.allow_tags = True

        class Meta(PageBaseContent.Meta):
            app_label = 'pagesext'
            verbose_name = _('Image')
            verbose_name_plural = _('Images')

        class PageMeta(PageBaseContent.PageMeta):
            context_name = 'images'
            multiple_per_page = True
            multiple_per_locale = True

    # Signals handler for deleting files after object record deleted
    @receiver(post_delete, sender=PageImageContent)
    def delete_image(sender, **kwargs):
        """Automatically delete image file when records removed."""
        if settings.PAGES_EXT_DELETE_IMAGE_FILE:
            image = kwargs.get('instance')
            if image.image is not None:
                try:
                    image.image.storage.delete(image.image.path)
                except Exception:
                    pass
