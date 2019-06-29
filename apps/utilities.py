"""Utilities."""

# Urls
from django.urls import reverse


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
