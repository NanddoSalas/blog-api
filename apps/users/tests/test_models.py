"""User models tests."""

# Django
from django.test import TestCase

# Models
from apps.users.models import User

# Exceptions
from django.db.utils import IntegrityError

class UserTest(TestCase):
    """Test the User model."""

    def create_user(self):
        """Create a new user."""
        data = {
            'username': 'root',
            'password': 'L!nux123',
            'email': 'root@localhost',
        }
        return User.objects.create_user(**data)

    def test_user_creation(self):
        """Test user creation."""
        user = self.create_user()
        self.assertIsInstance(user, User)
        self.assertEqual(str(user), user.username)
        self.assertFalse(user.is_verified)
        with self.assertRaises(IntegrityError) as error:
            user = self.create_user()