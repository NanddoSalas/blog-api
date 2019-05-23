"""User serializers tests."""

# Django
from django.test import TestCase

# Serializers
from apps.users.serializers import UserSignUpSerializer

# Models
from apps.users.models import User

# Utilities
from apps.utilities import SerializerUtilities

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

        user = User.objects.create_user(**data1)
        serializer = self.get_serializer(data=data2)

        self.assertFalse(serializer.is_valid())

        username_error = serializer.errors['username'][0]
        email_error = serializer.errors['email'][0]

        self.assertEqual(username_error.code, 'unique')
        self.assertEqual(email_error.code, 'unique')