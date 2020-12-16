from django.contrib.auth import get_user_model, authenticate
from django.db.models import Model
from django.test import TestCase


class LoginTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='name_admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user

    def test_wrong_user_name(self):
        user = authenticate(username='wrong', password='admin')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_user_password(self):
        user = authenticate(username='name_admin', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_success_login(self):
        user = authenticate(username='name_admin', password='admin')
        self.assertTrue(user is not None and user.is_authenticated)
