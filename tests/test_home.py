from tests.test_case import AppTestCase


class ViewTests(AppTestCase):

    def test_200_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
