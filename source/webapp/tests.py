from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.db.models import Model
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse

from webapp.models import Category, Article, MainCategory

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


class LoginArticleTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('loaddata', 'fixtures/auth.json', verbosity=0)
        call_command('loaddata', 'fixtures/dump.json', verbosity=0)
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin1')
        if created:
            user.set_password('admin1')
            user.save()
        cls.user = user

    def setUp(self) -> None:
        self.client.login(username='admin1', password='admin1')
        url = reverse('webapp:article_create')
        self.category = Category.objects.first()
        self.data = {'title': 'TestArticle', 'description': 'TestDescription',
                     'category_id': self.category.pk, 'user_id': self.user}
        self.response = self.client.post(url, self.data)
        self.article = Article.objects.order_by('pk').last()

    def tearDown(self) -> None:
        self.client.logout()

    def test_create_article_success(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(type(self.response), HttpResponseRedirect)
        redirect_url = reverse('webapp:article_view', kwargs={'pk': self.article.pk})
        self.assertEqual(self.response.url, redirect_url)

    def test_article_create_success_data(self):
        article_category = self.article.category_id.values_list('pk')
        self.assertEqual(self.article.title, self.data['title'])
        self.assertEqual(self.article.description, self.data['description'])
        self.assertIn(self.category.pk, article_category[0])
        self.assertEqual(self.article.user_id, self.data['user_id'])


class LoginMainCategoryTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('loaddata', 'fixtures/auth.json', verbosity=0)
        call_command('loaddata', 'fixtures/dump.json', verbosity=0)
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin1')
        if created:
            user.set_password('admin1')
            user.save()
        cls.user = user

    def setUp(self) -> None:
        self.client.login(username='admin1', password='admin1')
        url = reverse('webapp:main_category_create')
        self.data = {'title': 'TestMainCategory'}
        self.response = self.client.post(url, self.data)
        self.main_category = MainCategory.objects.order_by('pk').last()

    def tearDown(self) -> None:
        self.client.logout()

    def test_create_article_success(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(type(self.response), HttpResponseRedirect)
        redirect_url = reverse('webapp:main_category_view', kwargs={'pk': self.main_category.pk})
        self.assertEqual(self.response.url, redirect_url)

    def test_article_create_success_data(self):
        self.assertEqual(self.main_category.title, self.data['title'])


class LoginCategoryTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('loaddata', 'fixtures/auth.json', verbosity=0)
        call_command('loaddata', 'fixtures/dump.json', verbosity=0)
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin1')
        if created:
            user.set_password('admin1')
            user.save()
        cls.user = user

    def setUp(self) -> None:
        self.client.login(username='admin1', password='admin1')
        url = reverse('webapp:category_create')
        main_category = MainCategory.objects.first()
        self.data = {'title': 'TestCategory', 'parent_id': main_category.pk}
        self.response = self.client.post(url, self.data)
        self.category = Category.objects.order_by('pk').last()

    def tearDown(self) -> None:
        self.client.logout()

    def test_create_article_success(self):
        self.assertEqual(self.response.status_code, 302)
        self.assertEqual(type(self.response), HttpResponseRedirect)
        redirect_url = reverse('webapp:category_news', kwargs={'pk': self.category.pk})
        self.assertEqual(self.response.url, redirect_url)

    def test_article_create_success_data(self):
        self.assertEqual(self.category.title, self.data['title'])
        self.assertEqual(self.category.parent_id.pk, self.data['parent_id'])


class LoginCategoryArticleTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('loaddata', 'fixtures/auth.json', verbosity=0)
        call_command('loaddata', 'fixtures/dump.json', verbosity=0)
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin1')
        if created:
            user.set_password('admin1')
            user.save()
        cls.user = user

    def setUp(self) -> None:
        self.client.login(username='admin1', password='admin1')
        self.category = Category.objects.first()
        url = reverse('webapp:category_news', kwargs={'pk': self.category.pk})
        self.response = self.client.get(url)

    def tearDown(self) -> None:
        self.client.logout()

    def test_get_category_success_response(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(type(self.response), TemplateResponse)

    def test_get_category_success_data(self):
        self.assertIn('articles', self.response.context)
        self.assertIn('category', self.response.context)
        self.assertTrue(len(self.response.context['articles']) >= 1)


class LoginCategoryMainCategoryTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('loaddata', 'fixtures/auth.json', verbosity=0)
        call_command('loaddata', 'fixtures/dump.json', verbosity=0)
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin1')
        if created:
            user.set_password('admin1')
            user.save()
        cls.user = user

    def setUp(self) -> None:
        self.client.login(username='admin1', password='admin1')
        self.main_category = MainCategory.objects.first()
        url = reverse('webapp:main_category_view', kwargs={'pk': self.main_category.pk})
        self.response = self.client.get(url)

    def tearDown(self) -> None:
        self.client.logout()

    def test_get_main_category_success_response(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(type(self.response), TemplateResponse)

    def test_get_main_category_success_data(self):
        self.assertIn('maincategory', self.response.context)
        self.assertIn('categories', self.response.context)
        self.assertTrue(len(self.response.context['categories']) >= 1)
