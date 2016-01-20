from django import template

from pages.templatetags.pages_tags import get_page_object_by_id

register = template.Library()


@register.simple_tag(takes_context=True)
def page_tags_by_id(context, oid):
    obj = get_page_object_by_id(context, 'tags', oid)
    return obj if obj else None


@register.assignment_tag(takes_context=True)
def get_page_tags_by_id(context, oid):
    return page_tags_by_id(context, oid)


@register.simple_tag(takes_context=True)
def page_image_by_id(context, oid):
    obj = get_page_object_by_id(context, 'image', oid)
    return obj if obj else None


@register.assignment_tag(takes_context=True)
def get_page_image_by_id(context, oid):
    return page_image_by_id(context, oid)


@register.simple_tag(takes_context=True)
def page_video_by_id(context, oid):
    obj = get_page_object_by_id(context, 'video', oid)
    return obj if obj else None


@register.assignment_tag(takes_context=True)
def get_page_video_by_id(context, oid):
    return page_video_by_id(context, oid)


@register.simple_tag(takes_context=True)
def page_file_by_id(context, oid):
    obj = get_page_object_by_id(context, 'file', oid)
    return obj if obj else None


@register.assignment_tag(takes_context=True)
def get_page_file_by_id(context, oid):
    return page_file_by_id(context, oid)
