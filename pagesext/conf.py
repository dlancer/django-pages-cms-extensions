from django.conf import settings
from appconf import AppConf


class PagesExtAppConf(AppConf):
    FILE_LOCATION = getattr(settings, 'PAGES_EXT_FILE_LOCATION', settings.MEDIA_ROOT)
    FILE_UPLOAD_PERMISSIONS = getattr(
        settings, 'PAGES_EXT_FILE_UPLOAD_PERMISSIONS', settings.FILE_UPLOAD_PERMISSIONS)

    FILE_UPLOAD_DIRECTORY_PERMISSIONS = getattr(
            settings, 'PAGES_EXT_FILE_UPLOAD_DIRECTORY_PERMISSIONS', settings.FILE_UPLOAD_DIRECTORY_PERMISSIONS)

    FILE_OVERWRITE_EXISTS = getattr(settings, 'PAGES_EXT_FILE_OVERWRITE_EXISTS', True)

    IMAGE_DIR = getattr(settings, 'PAGES_EXT_IMAGE_DIR', 'pages/images')
    IMAGE_WIDTH_MAX = getattr(settings, 'PAGES_EXT_IMAGE_WIDTH_MAX', 600)
    IMAGE_HEIGHT_MAX = getattr(settings, 'PAGES_EXT_IMAGE_HEIGHT_MAX', 800)
    IMAGE_USE_ORIGINAL_FILENAME = getattr(settings, 'PAGE_EXT_IMAGE_USE_ORIGINAL_FILENAME', False)
    DELETE_IMAGE_FILE = getattr(settings, 'PAGES_EXT_DELETE_IMAGE_FILE', False)

    FILE_DIR = getattr(settings, 'PAGES_EXT_FILE_DIR', 'pages/files')
    FILE_USE_ORIGINAL_FILENAME = getattr(settings, 'PAGE_EXT_FILE_USE_ORIGINAL_FILENAME', False)
    FILE_DELETE_FILE = getattr(settings, 'PAGE_EXT_FILE_DELETE_FILE', False)

    class Meta:
        prefix = 'pages_ext'
