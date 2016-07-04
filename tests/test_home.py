from django.test import TestCase


class ViewTests(TestCase):

    def test_200_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
