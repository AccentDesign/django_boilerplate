from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from authentication.models import User, UserManager
from tests.test_case import AppTestCase


class ModelTests(AppTestCase):

    ##################################
    # class                          #
    ##################################

    def test_base_class_is_abstract_base_user(self):
        self.assertTrue(issubclass(User, AbstractBaseUser))

    def test_base_class_is_permissions_mixin(self):
        self.assertTrue(issubclass(User, PermissionsMixin))

    ##################################
    # fields                         #
    ##################################

    def test_first_name(self):
        field = User._meta.get_field('first_name')
        self.assertEqual(field.max_length, 30)
        self.assertTrue(field.blank)

    def test_last_name(self):
        field = User._meta.get_field('last_name')
        self.assertEqual(field.max_length, 30)
        self.assertTrue(field.blank)

    def test_email(self):
        field = User._meta.get_field('email')
        self.assertTrue(field.unique)

    def test_is_staff(self):
        field = User._meta.get_field('is_staff')
        self.assertEqual(field.default, False)

    def test_is_active(self):
        field = User._meta.get_field('is_active')
        self.assertEqual(field.default, True)

    def test_date_joined(self):
        field = User._meta.get_field('date_joined')
        self.assertEqual(field.auto_now_add, True)

    ##################################
    # auth only specifics            #
    ##################################

    def test_email_as_username(self):
        self.assertEqual(User.USERNAME_FIELD, 'email')

    def test_required_fields_for_manager(self):
        self.assertListEqual(User.REQUIRED_FIELDS, ['first_name', 'last_name'])

    ##################################
    # meta                           #
    ##################################
    def test_default_ordering(self):
        user_1 = self.create_user(email='zoe@example.com')
        user_2 = self.create_user(email='billy@example.com')
        user_3 = self.create_user(email='sammy@example.com')
        self.assertListEqual(list(User.objects.all()), [user_2, user_3, user_1])

    ##################################
    # methods                        #
    ##################################

    def test_str_method(self):
        user = User(email='admin@example.com')
        self.assertEqual(user.__str__(), 'admin@example.com')

    def test_get_full_name(self):
        user = User(first_name='Admin', last_name='User')
        self.assertEqual(user.get_full_name(), 'Admin User')

    def test_get_short_name(self):
        user = User(first_name='Admin', last_name='User')
        self.assertEqual(user.get_short_name(), 'Admin')


class ModelManagerTests(AppTestCase):

    ##################################
    # class                          #
    ##################################

    def test_base_class_is_base_user_manager(self):
        self.assertTrue(issubclass(UserManager, BaseUserManager))

    ##################################
    # method create_user             #
    ##################################

    def test_create_user_takes_email_as_default(self):
        user = User.objects.create_user('bob@example.com', 'password')
        self.assertEqual(user.email, 'bob@example.com')

    def test_create_user_sets_is_staff_false(self):
        user = User.objects.create_user('bob@example.com', 'password')
        self.assertFalse(user.is_staff)

    def test_create_user_sets_is_superuser_false(self):
        user = User.objects.create_user('bob@example.com', 'password')
        self.assertFalse(user.is_superuser)

    def test_create_user_takes_extra_fields(self):
        user = User.objects.create_user('bob@example.com', 'password', first_name='Bob', last_name='Hope')
        self.assertEqual(user.first_name, 'Bob')
        self.assertEqual(user.last_name, 'Hope')

    ##################################
    # method create_superuser        #
    ##################################

    def test_create_superuser_takes_email_as_default(self):
        user = User.objects.create_superuser('admin@example.com', 'password')
        self.assertEqual(user.email, 'admin@example.com')

    def test_create_superuser_sets_is_staff_true(self):
        user = User.objects.create_superuser('admin@example.com', 'password')
        self.assertTrue(user.is_staff)

    def test_create_superuser_sets_is_superuser_true(self):
        user = User.objects.create_superuser('admin@example.com', 'password')
        self.assertTrue(user.is_superuser)

    def test_create_superuser_takes_extra_fields(self):
        user = User.objects.create_superuser('admin@example.com', 'password', first_name='Admin', last_name='User')
        self.assertEqual(user.first_name, 'Admin')
        self.assertEqual(user.last_name, 'User')

    def test_passing_is_staff_false_to_create_superuser_raised_value_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser('admin@example.com', 'password', is_staff=False)

    def test_passing_is_superuser_false_to_create_superuser_raised_value_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser('admin@example.com', 'password', is_superuser=False)
