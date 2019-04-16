"""Users Serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.users.models import User

# Validators
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


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
            'email'
        )


class UserSignUpSerializer(serializers.Serializer):
    """User SignUp Serializer."""

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Email already in use'
            )
        ]
    )

    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Username already in use'
            )
        ]
    )

    first_name = serializers.CharField(
        max_length=30,
        required=False
    )

    last_name = serializers.CharField(
        max_length=30,
        required=False
    )

    password = serializers.CharField()
    password2 = serializers.CharField()

    def validate(self, data):
        """Verify that the passwords match and validate and validates using AUTH_PASSWORD_VALIDATORS."""
        password1 = data.get('password')
        password2 = data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise serializers.ValidationError({'password': "Passwords don't match"})
            validate_password(password=password1)
        return data

    def create(self, data):
        """Create user and return it."""
        data.pop('password2')
        return User.objects.create_user(**data)