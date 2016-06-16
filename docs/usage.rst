Usage
=====

Start the development server and visit http://127.0.0.1:8000/admin/ to setup
content management system settings (you'll need the Admin app enabled).

Visit http://127.0.0.1:8000/ to use content management system.

Configuration
=============

You must add these apps to your list of ``INSTALLED_APPS`` in ``settings.py``::

    INSTALLED_APPS = (
        ...
        'guardian',
        'mptt',
        'markitup',
        'easy_thumbnails',
        'image_cropping',
        'embed_video',
        'taggit',
        'pages',
        'pagesext',
    )


Include content management system URLconf in your project urls.py like this::

    urlpatterns = i18n_patterns(url(r'^page/', include('pages.urls', namespace='pages')),)

Run ``python manage.py migrate``.
This creates the appropriate tables in your database that are necessary for operation.

After database creation you must load extended content types to database from provided fixtures::

    $ python manage.py loaddata ext_content_types


Database migration
------------------

Django 1.7+ has native database migration support.

Multilingual support
--------------------

All messages and text strings translatable with standard Django i18n framework.
You may use multilingual content for your pages. Default language is English.

Extended content types
======================

Extended content types support is disabled by default, if you want use extended content types
you should setup these options in your django project settings:

* ``PAGES_PAGE_USE_EXT_CONTENT_TYPES`` = True
* ``PAGES_PAGE_EXT_CONTENT_TYPES`` = list(your extend content types models)
* ``PAGES_PAGE_EXT_CONTENT_INLINES`` = list(your extend content types inlines for admin panel)

You also should add your extended content types to PageContentType table.


Customizing content management system
-------------------------------------

You have a lot of options available to you to customize ``django-pages-cms-extensions``.
These options should be defined in your ``settings.py`` file.

**CMS file system settings**

* ``PAGES_EXT_FILE_LOCATION``: directory for uploading files (default is Django MEDIA_ROOT)
* ``PAGES_EXT_FILE_UPLOAD_PERMISSIONS``: permissions for uploading files
* ``PAGES_EXT_FILE_UPLOAD_DIRECTORY_PERMISSIONS``: permissions for uploading directory
* ``PAGES_EXT_FILE_OVERWRITE_EXISTS``: overwrite file with existed filename (default: True)

**CMS image type settings**

* ``PAGES_EXT_IMAGE_DIR``: directory for images (default: 'pages/images')
* ``PAGES_EXT_IMAGE_WIDTH_MAX``: maximum width for images
* ``PAGES_EXT_IMAGE_HEIGHT_MAX``: maximum height for images
* ``PAGES_EXT_IMAGE_USE_ORIGINAL_FILENAME``: use original filename for uploading image (default: False)
* ``PAGES_EXT_DELETE_IMAGE_FILE``: delete image file for deleted image object (default: False)

**CMS file type settings**

* ``PAGES_EXT_FILE_DIR``: directory for files (default: 'pages/files')
* ``PAGES_EXT_FILE_USE_ORIGINAL_FILENAME``: use original filename for uploading file (default: False)
* ``PAGES_EXT_FILE_DELETE_FILE``: delete file for deleted file object (default: False)

