"""Implements page tags extended content model"""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager

from pages.conf import settings
from pages.models.pagebasecontent import PageBaseContent

if settings.PAGES_PAGE_USE_EXT_CONTENT_TYPES:

    class PageTagsContent(PageBaseContent):
        tags = TaggableManager()
        objects = models.Manager()

        def add(self, *args):
            return self.tags.add(*args)

        def remove(self, *args):
            return self.tags.remove(*args)

        def set(self, *args):
            return self.tags.set(*args)

        def clear(self):
            return self.tags.clear()

        def names(self):
            return self.tags.names()

        def similar_objects(self):
            return self.tags.similar_objects()

        def slugs(self):
            return self.tags.slugs()

        def update_fields(self, change):
            if not change:
                self.type = 'tags'
                self.is_extended = True

        class Meta(PageBaseContent.Meta):
            app_label = 'pagesext'
            verbose_name = _('Tags')
            verbose_name_plural = _('Tags')

        class PageMeta(PageBaseContent.PageMeta):
            context_name = 'tags'
            multiple_per_page = True
            multiple_per_locale = True
