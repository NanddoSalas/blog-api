"""Post Views."""

# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    CreateModelMixin
)

# Models
from apps.posts.models import Post

# Serializers
from apps.posts.serializers import PostModelSerializer

# Permissions
from apps.posts.permissions import IsPostOwner
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

# Filters
from rest_framework.filters import (
    SearchFilter,
)
from django_filters.rest_framework import DjangoFilterBackend
from apps.posts.filters import PostFilter


class PostViewSet(GenericViewSet,
                  CreateModelMixin,
                  ListModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin):
    """Post View Set"""

    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    
    filter_backends = (
        SearchFilter,
        DjangoFilterBackend,
    )

    search_fields = ('title',)
    filterset_class = PostFilter

    def get_permissions(self):
        """Assign permissions based on action."""
        permission_classes = []
        if self.action == 'create':
            permission_classes.append(IsAuthenticated)
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes.append(IsPostOwner)
        else:
            permission_classes.append(AllowAny)
        return [permission() for permission in permission_classes]