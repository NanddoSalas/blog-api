"""Utilities."""

# Django
from django.conf import settings

# Urls
from django.urls import reverse

# Models
from apps.users.models import User

# Utilities
import jwt


class SerializerUtilities():
    """Serializer utilities.

    Help you to write serializers test more easy.
    """

    serializer_class = None

    def get_serializer(self, *args, **kwargs):
        """Return the serializer instance with given args (data, context, etc)"""
        return self.serializer_class(*args, **kwargs)


class ViewSetTestUtilities():
    """Shortcuts for write viewset test more easy."""

    basename = None

    def get_action_url(self, action, *args, **kwargs):
        """Return the url based on action."""
        viewname = '{}-{}'.format(self.basename, action)
        return reverse(viewname, *args, **kwargs)


def get_email_by_user_pk(pk):
    """Retrive User's email by the given pk."""
    return User.objects.get(pk=pk).email


def get_email_v_token(email):
    """Create and return a JWT of type 'email_v' by the given email."""
    data = {
        'type': 'email_v',
        'email': email,
    }
    token = jwt.encode(
        payload=data,
        key=settings.SECRET_KEY,
        algorithm='HS256'
    )
    return token.decode()
