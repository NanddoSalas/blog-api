"""Comment Views."""

# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import get_object_or_404

# Mixins
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
)

# Models
from apps.posts.models import Post

# Serializers
from apps.posts.serializers import CommentModelSerializer

# Permissions
from apps.posts.permissions import IsCommentOwner
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)


class CommentViewSet(GenericViewSet,
                     ListModelMixin,
                     CreateModelMixin,
                     DestroyModelMixin):
    """Comment View Set."""

    serializer_class = CommentModelSerializer

    def dispatch(self, request, *args, **kwargs):
        """
        Get post or 404.

        Get post using post 'id' kwarg given per the url.
        """
        self.post_obj = get_object_or_404(Post, id=kwargs['id'])
        return super(CommentViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """Get all comments from the given post."""
        return self.post_obj.comment_set.all()

    def get_serializer_context(self):
        """Add post_obj to serializer context."""
        context = super(CommentViewSet, self).get_serializer_context()
        context['post'] = self.post_obj
        return context

    def get_permissions(self):
        """Assign permissions based on action."""
        permission_classes = []
        if self.action == 'create':
            permission_classes.append(IsAuthenticated)
        if self.action == 'destroy':
            permission_classes.append(IsCommentOwner)
        else:
            permission_classes.append(AllowAny)
        return [permission() for permission in permission_classes]
