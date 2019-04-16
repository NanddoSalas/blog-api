"""SignUp Tests."""

# Django
from django.test import TestCase

# Django REST Framework
from rest_framework import status


class SignUpTestCase(TestCase):
    """SignUp test case."""

    def setUp(self):
        self.user_data = {
            'username': 'root',
            'email': 'root@localhost',
            'password': 'L!nux363230',
            'password2': 'L!nux363230',
        }
        self.url = '/users/signup/'

    def test_signup(self):
        response = self.client.post(
            self.url,
            self.user_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)