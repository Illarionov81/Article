from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.db.models import Model
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse

from webapp.models import Category, Article

GET_URL_PK = [
    'webapp:article_view',
    'webapp:article_delete',
    'webapp:article_update',

    'webapp:main_category_delete',
    'webapp:main_category_view',
    'webapp:main_category_update',

    'webapp:category_delete',
    'webapp:category_update',
    'webapp:category_news',

    'accounts:delete',
    'accounts:detail',
]
URLS_NO_PK = [
    'webapp:article_create',
    'webapp:articles_view',

    'webapp:main_category_create',
    'webapp:main_categories_view',

    'webapp:category_create',
    'webapp:categories_view',

    'accounts:users',
]


class UnLoginTestCase(TestCase):
    def test_get_not_login_pk(self):
        for url in GET_URL_PK:
            redirect_url = reverse('accounts:login') + '?next=' + reverse(url, kwargs={'pk': 1})
            response = self.client.get(reverse(url, kwargs={'pk': 1}))
            self.check_redirect(response, redirect_url)

    def test_get_not_login_no_pk(self):
        for url in URLS_NO_PK:
            redirect_url = reverse('accounts:login') + '?next=' + reverse(url)
            response = self.client.get(reverse(url))
            self.check_redirect(response, redirect_url)

    def test_post_not_login(self):
        for url in GET_URL_PK:
            redirect_url = reverse('accounts:login') + '?next=' + reverse(url, kwargs={'pk': 1})
            response = self.client.post(reverse(url, kwargs={'pk': 1}))
            self.check_redirect(response, redirect_url)

    def test_post_not_login_no_pk(self):
        for url in URLS_NO_PK:
            redirect_url = reverse('accounts:login') + '?next=' + reverse(url)
            response = self.client.post(reverse(url))
            self.check_redirect(response, redirect_url)

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)


