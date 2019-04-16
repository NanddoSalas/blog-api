"""Login Tests."""

# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Models
from apps.users.models import User
from rest_framework.authtoken.models import Token


class LoginAPITestCase(APITestCase):
    """Login API Test Case."""

    def setUp(self):

        self.user = User.objects.create_user(
            username='login',
            email='login@localhost',
            password='L0gin123'
        )

        self.LOGIN_URL = '/users/login/'

    def test_login(self):
        response = self.client.post(
            self.LOGIN_URL,
            {
                'email': 'login@localhost',
                'password': 'L0gin123'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        token = Token.objects.get(user=self.user).key
        self.assertEqual(
            token,
            response.data['token']
        )