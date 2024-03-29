"""User serializers tests."""

# Django
from django.test import TestCase

# Serializers
from apps.users.serializers import (
    UserSignUpSerializer,
    UserLoginSerializer,
    EmailVerificationSerializer,
    UserModelSerializer,
)

# Models
from apps.users.models import User
from rest_framework.authtoken.models import Token

# Utilities
from apps.users.tasks import get_email_v_token
from apps.utilities import SerializerUtilities
from django.utils import timezone


class UserSignUpSerializerTest(TestCase, SerializerUtilities):
    """Test UserSignUpSerializer."""

    serializer_class = UserSignUpSerializer
    user_data = {
        'username': 'root',
        'email': 'root@localhost',
        'password': 'L!nux123',
        'password2': 'L!nux123'
    }

    def test_validate_empty_data(self):
        """Validate with empty data."""
        serializer = self.get_serializer(data={})

        self.assertFalse(serializer.is_valid())

    def test_save(self):
        """Validate with true data."""
        data = self.user_data.copy()
        serializer = self.get_serializer(data=data)

        self.assertTrue(serializer.is_valid())

        user = serializer.save()

        self.assertIsInstance(user, User)

    def test_passwords_do_not_match(self):
        """Passwords don't match test."""
        data = self.user_data.copy()
        data['password'] = 'Linux123'
        serializer = self.get_serializer(data=data)

        self.assertFalse(serializer.is_valid())

        password_error = serializer.errors['password'][0]

        self.assertEqual(str(password_error), "Passwords don't match")

    def test_unique_fileds(self):
        """Test the uniquie fields (username, email)."""
        data1 = self.user_data.copy()
        data2 = self.user_data.copy()
        data1.pop('password2')

        User.objects.create_user(**data1)
        serializer = self.get_serializer(data=data2)

        self.assertFalse(serializer.is_valid())

        username_error = serializer.errors['username'][0]
        email_error = serializer.errors['email'][0]

        self.assertEqual(username_error.code, 'unique')
        self.assertEqual(email_error.code, 'unique')


class UserLoginSerializerTest(TestCase, SerializerUtilities):
    """Test UserLoginSerializer."""

    serializer_class = UserLoginSerializer

    def setUp(self):
        # Create a test user.

        self.user_data = {
            'username': 'Test',
            'email': 'test@localhost',
            'password': 'L!nux123',
        }

        self.user = User.objects.create_user(**self.user_data)

    def test_unverified_email(self):
        """Test the users's login with a unverified email."""
        data = {
            'email': 'test@localhost',
            'password': 'L!nux123',
        }
        serializer = self.get_serializer(data=data)
        self.assertFalse(serializer.is_valid())

        message_error = serializer.errors['message'][0]
        self.assertEqual(str(message_error), 'Verify you email')

    def test_invalid_credentials(self):
        """Test the login for a non-existent user."""
        data = {
            'email': 'root@localhost',
            'password': 'toor',
        }
        serializer = self.get_serializer(data=data)
        self.assertFalse(serializer.is_valid())

        message_error = serializer.errors['message'][0]
        self.assertEqual(str(message_error), 'Invalid credentials')

    def test_valid_credentials(self):
        """Test login."""

        # Verify user's email
        user = self.user
        user.is_verified = True
        user.save()

        data = {
            'email': 'test@localhost',
            'password': 'L!nux123',
        }

        serializer = self.get_serializer(data=data)
        self.assertTrue(serializer.is_valid())

        token, user = serializer.save()
        self.assertTrue(
            Token.objects.filter(
                user=user,
                key=token
            ).exists()
        )


class EmailVerificationSerializerTest(TestCase, SerializerUtilities):
    """Test EmailVerificationSerializer."""

    serializer_class = EmailVerificationSerializer

    def setUp(self):
        """Create a user and get his JWT."""
        data = {
            'username': 'Test',
            'email': 'test@localhost',
            'password': 'L!nux123',
        }

        self.user = User.objects.create_user(**data)
        self.token = get_email_v_token(self.user.email)

    def test_invalid_token(self):
        """Test with a invalid token."""
        data = {
            'token': 'THIS_IS_A_INVALID_TOKEN'
        }
        serializer = self.get_serializer(data=data)
        self.assertFalse(serializer.is_valid())

        token_error = serializer.errors['token'][0]
        self.assertEqual(str(token_error), 'Invalid Token')

    def test_valid_token_and_save(self):
        """Test the full prosses with a valid jwt."""
        user = self.user
        data = {
            'token': self.token
        }
        serializer = self.get_serializer(data=data)
        self.assertTrue(serializer.is_valid())

        serializer.save()
        user.refresh_from_db()

        self.assertTrue(user.is_verified)


class UserModelSerializerTest(TestCase, SerializerUtilities):
    """Test UserModelSerializerTest."""

    serializer_class = UserModelSerializer

    def setUp(self):
        # Create a test user.

        self.user_data = {
            'username': 'Test',
            'first_name': 'root',
            'last_name': 'toor',
            'email': 'test@localhost',
            'password': 'L!nux123',
        }

        self.user = User.objects.create_user(**self.user_data)

    def test_get_data(self):
        """Serialize a python model to json."""
        user = self.user
        user_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name
        }

        serializer_data = self.get_serializer(user).data
        serializer_data.pop('date_joined')  # ojo

        self.assertDictEqual(user_data, serializer_data)

    def test_update_allowed_fields(self):
        """Update fields (username, email, first_name, last_name)."""
        user = self.user
        new_data = {
            'username': 'tEST',
            'first_name': 'ROOT',
            'last_name': 'TOOR',
        }
        serializer = self.get_serializer(user, data=new_data)

        self.assertTrue(serializer.is_valid())

        user.refresh_from_db()
        data = serializer.data

        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.first_name, data['first_name'])
        self.assertEqual(user.last_name, data['last_name'])

    def test_red_only_fields(self):
        """Try to update read-only fields, without waiting for a change."""
        user = self.user
        user_copy = user
        new_data = {
            'date_joined': str(timezone.now()),
            'email': 'newtest@localhost'
        }
        serializer = self.get_serializer(user, data=new_data, partial=True)

        self.assertTrue(serializer.is_valid())

        user.refresh_from_db()
        self.assertEqual(user, user_copy)
