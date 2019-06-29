"""User views test."""

# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Utilities
from apps.utilities import ViewSetTestUtilities

# Models
from apps.users.models import User


class UserViewSetTest(APITestCase, ViewSetTestUtilities):
    """Test UserViewSet endpoinds."""

    basename = 'users'

    def test_signup(self):
        """Test signup endpoind."""

        signup_data = {
            'username': 'test',
            'email': 'test@localhost',
            'first_name': 'root',
            'last_name': 'toor',
            'password': 'L!nux123',
            'password2': 'L!nux123'
        }

        url = self.get_action_url('signup')
        response = self.client.post(url, signup_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_data = response.data.copy()
        response_data.pop('date_joined')
        signup_data.pop('password')
        signup_data.pop('password2')

        self.assertDictEqual(response_data, signup_data)

        try:
            user = User.objects.get(**response_data)
            self.assertIsInstance(user, User)
        except User.DoesNotExist:
            self.assertFalse(True)
