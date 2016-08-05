from authentication.forms import UserCreationForm, UserChangeForm
from authentication.models import User
from tests.test_case import AppTestCase


class UserCreationFormTests(AppTestCase):

    def setUp(self):
        self.data = {
            'email': 'user@example.com',
            'first_name': 'Some',
            'last_name': 'One',
            'password1': 'password',
            'password2': 'password'
        }

    def test_meta_model(self):
        self.assertEqual(UserCreationForm().Meta.model, User)

    def test_meta_fields(self):
        self.assertEqual(UserCreationForm().Meta.fields, ('email', 'first_name', 'last_name'))

    def test_valid_form_saves(self):
        form = UserCreationForm(self.data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.email, 'user@example.com')
        self.assertEqual(user.first_name, 'Some')
        self.assertEqual(user.last_name, 'One')
        self.assertTrue(user.check_password('password'))

    def test_password_mismatch_raises_error(self):
        self.data['password2'] = 'foo'
        form = UserCreationForm(self.data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'password2': ["Passwords don't match"],
        })


class UserChangeFormTests(AppTestCase):

    def setUp(self):
        self.data = {
            'email': 'foo@example.com',
            'first_name': 'Some',
            'last_name': 'One'
        }

    def test_meta_model(self):
        self.assertEqual(UserChangeForm().Meta.model, User)

    def test_meta_exclude(self):
        self.assertEqual(UserChangeForm().Meta.exclude, ('password',))

    def test_valid_form_saves(self):
        instance = self.create_user(email='user@example.com', password='password')
        form = UserChangeForm(self.data, instance=instance)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.id, instance.id)
        self.assertEqual(user.email, 'foo@example.com')
        self.assertEqual(user.first_name, 'Some')
        self.assertEqual(user.last_name, 'One')
