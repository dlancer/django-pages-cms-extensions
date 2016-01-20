"""Implements admin interface for page tags content"""

from django.contrib import admin

from pages.conf import settings

if settings.PAGES_PAGE_USE_EXT_CONTENT_TYPES:
    from pagesext.models.pagetagscontent import PageTagsContent

    class PageTagsContentAdmin(admin.ModelAdmin):
        list_display = ('__str__', 'created_by', 'updated_by', 'date_created', 'date_updated',)
        list_display_links = ['__str__']
        fieldsets = [
            (None, {'fields': [
                ('language', ),
                ('name', ),
                ('tags', ),
                ('comment', ),
            ]}),
        ]

        exclude = ('type', 'sid', 'is_extended', 'created_by', 'updated_by',)
        save_on_top = True
        actions_on_bottom = True

    admin.site.register(PageTagsContent, PageTagsContentAdmin)

    class PageTagsContentInline(admin.StackedInline):
        model = PageTagsContent
        extra = 1
        exclude = ('sid', 'is_extended', 'created_by', 'updated_by', 'date_created', 'date_updated',)
        fieldsets = [
            (None, {'fields': [
                ('language', ),
                ('name', ),
                ('tags', ),
                ('comment', ),
            ]}),
        ]
