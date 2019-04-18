"""Comment Permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsCommentOwner(BasePermission):
    """Is Comment Owner."""

    def has_object_permission(self, request, view, obj):
        """Allow access to comment owner."""

        return request.user == obj.user