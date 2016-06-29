from django import template

from pagesext.models import PageImageContent, PageVideoContent, PageFileContent
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
def page_image_by_tag(context, tag):
    page = context['page']['page']
    images = PageImageContent.objects.filter(page=page, tags__name__in=[tag])
    return images[0] if len(images) else None


@register.assignment_tag(takes_context=True)
def get_page_image_by_tag(context, tag):
    page = context['page']['page']
    images = PageImageContent.objects.filter(page=page, tags__name__in=[tag])
    return images[0] if len(images) else None


@register.assignment_tag(takes_context=True)
def get_page_images_by_tags(context, tags):
    page = context['page']['page']
    images = PageImageContent.objects.filter(page=page, tags__name__in=[tags])
    return images


@register.simple_tag(takes_context=True)
def page_video_by_id(context, oid):
    obj = get_page_object_by_id(context, 'video', oid)
    return obj if obj else None


@register.assignment_tag(takes_context=True)
def get_page_video_by_id(context, oid):
    return page_video_by_id(context, oid)


@register.simple_tag(takes_context=True)
def page_video_by_tag(context, tag):
    page = context['page']['page']
    videos = PageVideoContent.objects.filter(page=page, tags__name__in=[tag])
    return videos[0] if len(videos) else None


@register.assignment_tag(takes_context=True)
def get_page_video_by_tag(context, tag):
    page = context['page']['page']
    videos = PageVideoContent.objects.filter(page=page, tags__name__in=[tag])
    return videos[0] if len(videos) else None


@register.assignment_tag(takes_context=True)
def get_page_videos_by_tags(context, tags):
    page = context['page']['page']
    videos = PageVideoContent.objects.filter(page=page, tags__name__in=[tags])
    return videos


@register.simple_tag(takes_context=True)
def page_file_by_id(context, oid):
    obj = get_page_object_by_id(context, 'file', oid)
    return obj if obj else None


@register.assignment_tag(takes_context=True)
def get_page_file_by_id(context, oid):
    return page_file_by_id(context, oid)


@register.simple_tag(takes_context=True)
def page_file_by_tag(context, tag):
    page = context['page']['page']
    files = PageFileContent.objects.filter(page=page, tags__name__in=[tag])
    return files[0] if len(files) else None


@register.assignment_tag(takes_context=True)
def get_page_file_by_tag(context, tag):
    page = context['page']['page']
    files = PageFileContent.objects.filter(page=page, tags__name__in=[tag])
    return files[0] if len(files) else None


@register.assignment_tag(takes_context=True)
def get_page_files_by_tags(context, tags):
    page = context['page']['page']
    files = PageFileContent.objects.filter(page=page, tags__name__in=[tags])
    return files
