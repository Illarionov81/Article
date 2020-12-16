import json

from django.core.management import call_command
from django.http import JsonResponse
from django.test import TestCase
from django.urls import reverse


URLS = ['api_v1:categories', 'api_v1:main_categories', 'api_v1:articles']


class GetJsonData(TestCase):
    def test_post_not_login_no_pk(self):
        for url in URLS:
            response = self.client.get(reverse(url))
            self.check_redirect(response)

    def check_redirect(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response), JsonResponse)


class UnLoginGetArticleJsonTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('loaddata', 'fixtures/auth.json', verbosity=0)
        call_command('loaddata', 'fixtures/dump.json', verbosity=0)

    def test_article_success_data(self):
        url = reverse('api_v1:articles')
        self.response = self.client.get(url)
        print(self.response)
        data = json.loads(self.response.content)
        self.assertTrue(len(data) >= 1)
        self.assertIn('pk', data[0])
        self.assertIn('title', data[0])
        self.assertIn('description', data[0])
        self.assertIn('category_id', data[0])
        self.assertIn('user_id', data[0])
        self.assertIn('image', data[0])

    def test_get_main_category_json_data(self):
        url = reverse('api_v1:main_categories')
        self.response = self.client.get(url)
        data = json.loads(self.response.content)
        self.assertTrue(len(data) >= 1)
        self.assertIn('pk', data[0])
        self.assertIn('title', data[0])

    def test_get_json_category_success_data(self):
        url = reverse('api_v1:categories')
        self.response = self.client.get(url)
        data = json.loads(self.response.content)
        self.assertTrue(len(data) >= 1)
        self.assertIn('pk', data[0])
        self.assertIn('title', data[0])
        self.assertIn('parent_id', data[0])
