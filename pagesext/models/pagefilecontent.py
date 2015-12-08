"""Implements page file extended content model"""

from __future__ import unicode_literals

import os
import uuid
import hashlib
import base64

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_delete
from django.dispatch import receiver

from pages.conf import settings
from pages.models.pagebasecontent import PageBaseContent
from pages.storage import PageFileSystemStorage
from pagesext.conf import settings as ext_settings

if settings.PAGES_PAGE_USE_EXT_CONTENT_TYPES:

    file_storage = PageFileSystemStorage()

    def make_file_upload_path(instance, filename, prefix=False):
        """Generate upload path and filename for file"""

        # store original filename
        instance.filename = filename
        ext = os.path.splitext(filename)[1].strip('.').lower()

        # always generate unique path, for security and file system balancing reasons
        file_uuid = uuid.uuid4().hex

        # generate short sha1 based hash
        name_sha = hashlib.sha1(file_uuid).digest()
        name_hash = base64.urlsafe_b64encode(name_sha[:9]).decode('utf-8')

        if ext_settings.PAGES_EXT_FILE_USE_ORIGINAL_FILENAME:
            name = file_storage.get_available_name(os.path.splitext(filename)[0])
        else:
            name = name_hash

        return u'{path}/{sub0}/{sub1}/{sub2}/{name}.{ext}'.format(
            path=ext_settings.PAGES_EXT_FILE_DIR,
            sub0=file_uuid[0:2],
            sub1=file_uuid[7:9],
            sub2=file_uuid[12:14],
            name=name,
            ext=ext
        )

    class PageFileContent(PageBaseContent):
        file = models.FileField(blank=True, null=True, upload_to=make_file_upload_path, storage=file_storage)
        title = models.CharField(max_length=160, blank=True)
        description = models.TextField(max_length=160, blank=True)
        objects = models.Manager()

        def update_fields(self, change):
            if not change:
                self.type = 'file'
                self.is_extended = True

        class Meta(PageBaseContent.Meta):
            app_label = 'pagesext'
            verbose_name = _('File')
            verbose_name_plural = _('File')

        class PageMeta(PageBaseContent.PageMeta):
            context_name = 'file'
            multiple_per_page = True
            multiple_per_locale = True

    # Signals handler for deleting files after object record deleted
    @receiver(post_delete, sender=PageFileContent)
    def delete_file(sender, **kwargs):
        """Automatically delete file when records removed."""
        if ext_settings.PAGES_EXT_FILE_DELETE_FILE:
            obj = kwargs.get('instance')
            if obj.file is not None:
                try:
                    obj.file.storage.delete(obj.file.path)
                except Exception:
                    pass
