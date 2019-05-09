"""Users models."""

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """User model.
    
    Change USERNAME_FILED to email.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    is_verifyed = models.BooleanField(
        'email is verifyed',
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        """Return username."""
        return self.username