"""Users Serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """User Model Serializer."""

    class Meta:
        """Meta Options."""

        model = User

        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined'
        )

        read_only_fields = (
            'date_joined',
        )