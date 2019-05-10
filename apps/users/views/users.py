"""Users Views."""

# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework import status
from rest_framework.response import Response

# Mixins
from rest_framework.mixins import (
    RetrieveModelMixin,
    UpdateModelMixin
)

# Models
from apps.users.models import User

# Serializers
from apps.users.serializers import (
    UserModelSerializer,
    UserSignUpSerializer,
    UserLoginSerializer,
    EmailVerificationSerializer,
)

# Decorators
from rest_framework.decorators import action

# Permissions
from rest_framework.permissions import AllowAny
from apps.users.permissions import IsAccountOwner


class UserViewSet(GenericViewSet,
                  RetrieveModelMixin,
                  UpdateModelMixin):

    queryset = User.objects.all()
    lookup_field = 'username'
    
    def get_permissions(self):
        """Assign permission based on action."""
        permission_classes = []
        if self.action in ['update', 'partial_update']:
            permission_classes.append(IsAccountOwner)
        else:
            permission_classes.append(AllowAny)
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """Retrieve Serializer based on action."""
        if self.action == 'login':
            return UserLoginSerializer
        if self.action == 'signup':
            return UserSignUpSerializer
        if self.action == 'verify':
            return EmailVerificationSerializer
        return UserModelSerializer

    @action(detail=False, methods=['POST'])
    def signup(self, request, *args, **kwargs):
        """Handle signup process."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def login(self, request, *args, **kwargs):
        """Handle login process.
        
        Retrieve token and user data if the credentials are valid.
        """
        serialzer = self.get_serializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        token, user = serialzer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'token': token
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def verify(self, request, *args, **kwargs):
        """Handle email verification process."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': 'Account is now active.'
        }
        return Response(data, status=status.HTTP_200_OK)