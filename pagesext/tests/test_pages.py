# -*- coding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import translation

from pages.cache import cache
from pages.models import PageSlugContent, PageMetaContent
from pages.models import PageTextContent
from pages.views import PageDetailsView
from pagesext.tests.base import PagesExtCase
from pagesext.models import PageTagsContent, PageImageContent, PageVideoContent, PageFileContent


class TestExtPages(PagesExtCase):
    def test_page_tags_model(self):
        PageTagsContent.objects.create(page=self.page_foo)
        obj = PageTagsContent.objects.filter(page=self.page_foo, language='en')[0]
        sid = obj.sid
        self.assertEqual(sid, 'en:Test:tags:1')
        obj.language = 'de'
        obj.save()
        self.assertEqual(obj.sid, 'de:Test:tags:1')

    def test_page_tags_api(self):
        PageTagsContent.objects.create(page=self.page_foo)
        obj = PageTagsContent.objects.filter(page=self.page_foo, language='en')[0]
        sid = obj.sid
        self.assertEqual(sid, 'en:Test:tags:1')
        obj.add('tag1', 'tag2')
        names = sorted(list(obj.tags.names()))
        self.assertEqual(names[0], 'tag1')
        self.assertEqual(names[1], 'tag2')
        obj.set('tag3', 'tag4')
        names = sorted(list(obj.tags.names()))
        self.assertEqual(names[0], 'tag3')
        self.assertEqual(names[1], 'tag4')
        slugs = sorted(list(obj.tags.slugs()))
        self.assertEqual(slugs[0], 'tag3')
        self.assertEqual(slugs[1], 'tag4')
        PageTagsContent.objects.create(page=self.page_foo2)
        obj2 = PageTagsContent.objects.filter(page=self.page_foo2, language='en')[0]
        obj2.add('tag4', 'tag5')
        objects = obj.similar_objects()
        self.assertEqual(objects[0], obj2)
        obj.remove('tag3')
        names = obj.tags.names()
        self.assertEqual(len(names), 1)
        obj.clear()
        names = obj.tags.names()
        self.assertEqual(len(names), 0)

    def test_page_image_model(self):
        PageImageContent.objects.create(page=self.page_foo)
        obj = PageImageContent.objects.filter(page=self.page_foo, language='en')[0]
        sid = obj.sid
        self.assertEqual(sid, 'en:Test:image:1')
        obj.language = 'de'
        obj.save()
        self.assertEqual(obj.sid, 'de:Test:image:1')

    def test_page_video_model(self):
        PageVideoContent.objects.create(page=self.page_foo)
        obj = PageVideoContent.objects.filter(page=self.page_foo, language='en')[0]
        sid = obj.sid
        self.assertEqual(sid, 'en:Test:video:1')
        obj.language = 'de'
        obj.save()
        self.assertEqual(obj.sid, 'de:Test:video:1')

    def test_page_file_model(self):
        PageFileContent.objects.create(page=self.page_foo)
        obj = PageFileContent.objects.filter(page=self.page_foo, language='en')[0]
        sid = obj.sid
        self.assertEqual(sid, 'en:Test:file:1')
        obj.language = 'de'
        obj.save()
        self.assertEqual(obj.sid, 'de:Test:file:1')

    def test_page_tags_view(self):
        PageSlugContent.objects.create(page=self.page_foo, slug='test')
        PageMetaContent.objects.create(page=self.page_foo, title='test', description='test', keywords='test')
        PageTextContent.objects.create(page=self.page_foo, text='test')
        PageTagsContent.objects.create(page=self.page_foo)
        obj = PageTagsContent.objects.filter(page=self.page_foo, language='en')[0]
        obj.add('tag1', 'tag2')
        self.page_foo.template = 'pages/page_tags.html'
        self.page_foo.save()
        page_url = reverse('pages:show', kwargs={'slug': 'test'})
        request = self.factory.get(page_url)
        request.user = AnonymousUser()
        context = RequestContext(request)
        view = PageDetailsView.as_view()
        translation.activate('en')
        response = view(request=request, context=context, slug='test')
        translation.deactivate()
        self.assertEqual(response.status_code, 200)
        self.page_foo.delete()
        cache.clear()

    def test_page_image_view(self):
        PageSlugContent.objects.create(page=self.page_foo, slug='test')
        PageMetaContent.objects.create(page=self.page_foo, title='test', description='test', keywords='test')
        PageTextContent.objects.create(page=self.page_foo, text='test')
        PageImageContent.objects.create(page=self.page_foo, image='img/test.jpg', title='test')

        img1 = PageImageContent.objects.create(page=self.page_foo, image='img/test.jpg', title='test')
        img1.tags.add('test', 'image-1')
        img2 = PageImageContent.objects.create(page=self.page_foo, image='img/test.jpg', title='test')
        img2.tags.add('test', 'image-2')

        self.page_foo.template = 'pages/page_image.html'
        self.page_foo.save()
        page_url = reverse('pages:show', kwargs={'slug': 'test'})
        request = self.factory.get(page_url)
        request.user = AnonymousUser()
        context = RequestContext(request)
        view = PageDetailsView.as_view()
        translation.activate('en')
        response = view(request=request, context=context, slug='test')

        translation.deactivate()
        self.assertEqual(response.status_code, 200)
        self.page_foo.delete()
        cache.clear()

    def test_page_video_view(self):
        PageSlugContent.objects.create(page=self.page_foo, slug='test')
        PageMetaContent.objects.create(page=self.page_foo, title='test', description='test', keywords='test')
        PageTextContent.objects.create(page=self.page_foo, text='test')
        PageVideoContent.objects.create(
            page=self.page_foo, video='https://www.youtube.com/watch?v=C0DPdy98e4c', title='test'
        )

        video1 = PageVideoContent.objects.create(
            page=self.page_foo, video='https://www.youtube.com/watch?v=C0DPdy98e4c', title='test'
        )
        video1.tags.add('test', 'video-1')
        video2 = PageVideoContent.objects.create(
            page=self.page_foo, video='https://www.youtube.com/watch?v=C0DPdy98e4c', title='test'
        )
        video2.tags.add('test', 'video-2')

        self.page_foo.template = 'pages/page_video.html'
        self.page_foo.save()
        page_url = reverse('pages:show', kwargs={'slug': 'test'})
        request = self.factory.get(page_url)
        request.user = AnonymousUser()
        context = RequestContext(request)
        view = PageDetailsView.as_view()
        translation.activate('en')
        response = view(request=request, context=context, slug='test')
        translation.deactivate()
        self.assertEqual(response.status_code, 200)
        self.page_foo.delete()
        cache.clear()

    def test_page_file_view(self):
        PageSlugContent.objects.create(page=self.page_foo, slug='test')
        PageMetaContent.objects.create(page=self.page_foo, title='test', description='test', keywords='test')
        PageTextContent.objects.create(page=self.page_foo, text='test')
        PageFileContent.objects.create(page=self.page_foo, file='files/test.txt', title='test')

        file1 = PageFileContent.objects.create(page=self.page_foo, file='files/test.txt', title='test')
        file1.tags.add('test', 'file-1')
        file2 = PageFileContent.objects.create(page=self.page_foo, file='files/test.txt', title='test')
        file2.tags.add('test', 'file-2')

        self.page_foo.template = 'pages/page_file.html'
        self.page_foo.save()
        page_url = reverse('pages:show', kwargs={'slug': 'test'})
        request = self.factory.get(page_url)
        request.user = AnonymousUser()
        context = RequestContext(request)
        view = PageDetailsView.as_view()
        translation.activate('en')
        response = view(request=request, context=context, slug='test')
        translation.deactivate()
        self.assertEqual(response.status_code, 200)
        self.page_foo.delete()
        cache.clear()
