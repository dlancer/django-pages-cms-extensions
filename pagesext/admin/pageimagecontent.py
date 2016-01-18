from django.contrib import admin

from image_cropping import ImageCroppingMixin

from pagesext.models import PageImageContent


class PageImageContentAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('__str__', 'created_by', 'updated_by', 'date_created', 'date_updated',)
    list_display_links = ['__str__']

    exclude = ('type', 'sid', 'is_extended', 'created_by', 'updated_by',)
    save_on_top = True
    actions_on_bottom = True

admin.site.register(PageImageContent, PageImageContentAdmin)


class PageImageContentInline(admin.StackedInline):
    model = PageImageContent
    extra = 1
    exclude = ('sid', 'created_by', 'updated_by', 'date_created', 'date_updated',)
    readonly_fields = ['image_cropping_link']
    fieldsets = [
        (None, {'fields': [
            ('language', ),
            ('name', ),
            ('image', ),
            ('image_cropping_link', ),
            ('title', ),
            ('tags', ),
            ('comment', ),
        ]}),
    ]
