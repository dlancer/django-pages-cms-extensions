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
from pagesext.models import PageVideoContent, PageFileContent


class TestExtPages(PagesExtCase):

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

    def test_page_video_view(self):
        PageSlugContent.objects.create(page=self.page_foo, slug='test')
        PageMetaContent.objects.create(page=self.page_foo, title='test', description='test', keywords='test')
        PageTextContent.objects.create(page=self.page_foo, text='test')
        PageVideoContent.objects.create(page=self.page_foo, video='xxx', title='test')
        self.page_foo.template = 'pages/page_video.html'
        self.page_foo.save()
        page_url = reverse('page_show', kwargs={'slug': 'test'})
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
        self.page_foo.template = 'pages/page_file.html'
        self.page_foo.save()
        page_url = reverse('page_show', kwargs={'slug': 'test'})
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
