"""Utilities."""

class SerializerUtilities():
    """Serializer utilities.

    Help you to write serializers test more easy.
    """

    serializer_class = None

    def get_serializer(self, *args, **kwargs):
        """Return the serializer instance with given args (data, context, etc)"""
        return self.serializer_class(*args, **kwargs)