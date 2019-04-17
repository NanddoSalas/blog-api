"""Post Views."""

# Django REST Framework
from rest_framework.viewsets import ModelViewSet

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


class PostViewSet(ModelViewSet):
    """Post View Set"""

    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

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