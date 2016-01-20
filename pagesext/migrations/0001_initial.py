# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pagesext.storage
import pagesext.models.pageimagecontent
import embed_video.fields
import pagesext.models.pagefilecontent
import django.utils.timezone
from django.conf import settings
import image_cropping.fields
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('pages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PageFileContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name='Type', db_index=True)),
                ('language', models.CharField(default=b'en', max_length=5)),
                ('sid', models.CharField(unique=True, max_length=200)),
                ('name', models.CharField(unique=True, max_length=200, blank=True)),
                ('is_extended', models.BooleanField(default=False, verbose_name='Extended?')),
                ('comment', models.CharField(max_length=250, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('file', models.FileField(storage=pagesext.storage.PageExtFileSystemStorage(), null=True, upload_to=pagesext.models.pagefilecontent.make_file_upload_path, blank=True)),
                ('title', models.CharField(max_length=160, blank=True)),
                ('description', models.TextField(max_length=160, blank=True)),
                ('created_by', models.ForeignKey(related_name='pagesext_pagefilecontent_creator', to=settings.AUTH_USER_MODEL, null=True)),
                ('page', models.ForeignKey(verbose_name='Page', to='pages.Page')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='pagesext_pagefilecontent_editor', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'File',
                'verbose_name_plural': 'File',
            },
        ),
        migrations.CreateModel(
            name='PageImageContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name='Type', db_index=True)),
                ('language', models.CharField(default=b'en', max_length=5)),
                ('sid', models.CharField(unique=True, max_length=200)),
                ('name', models.CharField(unique=True, max_length=200, blank=True)),
                ('is_extended', models.BooleanField(default=False, verbose_name='Extended?')),
                ('comment', models.CharField(max_length=250, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('image', image_cropping.fields.ImageCropField(storage=pagesext.storage.PageExtFileSystemStorage(), null=True, upload_to=pagesext.models.pageimagecontent.make_image_upload_path, blank=True)),
                ('cropping', image_cropping.fields.ImageRatioField('image', '600x800', hide_image_field=False, size_warning=True, allow_fullsize=True, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping')),
                ('title', models.CharField(max_length=250, blank=True)),
                ('created_by', models.ForeignKey(related_name='pagesext_pageimagecontent_creator', to=settings.AUTH_USER_MODEL, null=True)),
                ('page', models.ForeignKey(verbose_name='Page', to='pages.Page')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='pagesext_pageimagecontent_editor', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='PageTagsContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name='Type', db_index=True)),
                ('language', models.CharField(default=b'en', max_length=5)),
                ('sid', models.CharField(unique=True, max_length=200)),
                ('name', models.CharField(unique=True, max_length=200, blank=True)),
                ('is_extended', models.BooleanField(default=False, verbose_name='Extended?')),
                ('comment', models.CharField(max_length=250, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('created_by', models.ForeignKey(related_name='pagesext_pagetagscontent_creator', to=settings.AUTH_USER_MODEL, null=True)),
                ('page', models.ForeignKey(verbose_name='Page', to='pages.Page')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='pagesext_pagetagscontent_editor', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Tags',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='PageVideoContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100, verbose_name='Type', db_index=True)),
                ('language', models.CharField(default=b'en', max_length=5)),
                ('sid', models.CharField(unique=True, max_length=200)),
                ('name', models.CharField(unique=True, max_length=200, blank=True)),
                ('is_extended', models.BooleanField(default=False, verbose_name='Extended?')),
                ('comment', models.CharField(max_length=250, blank=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created')),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Updated')),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
                ('title', models.CharField(max_length=160, blank=True)),
                ('description', models.TextField(max_length=160, blank=True)),
                ('created_by', models.ForeignKey(related_name='pagesext_pagevideocontent_creator', to=settings.AUTH_USER_MODEL, null=True)),
                ('page', models.ForeignKey(verbose_name='Page', to='pages.Page')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('updated_by', models.ForeignKey(related_name='pagesext_pagevideocontent_editor', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Video',
                'verbose_name_plural': 'Video',
            },
        ),
    ]
