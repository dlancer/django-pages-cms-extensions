from django.conf import settings
from appconf import AppConf


class PagesExtAppConf(AppConf):
    FILE_DIR = getattr(settings, 'PAGES_EXT_FILE_DIR', 'pages/files')
    FILE_USE_ORIGINAL_FILENAME = getattr(settings, 'PAGE_EXT_FILE_USE_ORIGINAL_FILENAME', False)
    FILE_DELETE_FILE = getattr(settings, 'PAGE_EXT_FILE_DELETE_FILE', False)

    class Meta:
        prefix = 'pages_ext'
