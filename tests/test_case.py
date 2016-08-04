from django.test import TestCase

from authentication.models import User


class AppTestCase(TestCase):

    def create_user(self, email='user@example.com', password='password', **extra_fields):
        return User.objects.create_user(email, password, **extra_fields)

    def create_superuser(self, email='user@example.com', password='password', **extra_fields):
        return User.objects.create_superuser(email, password, **extra_fields)
