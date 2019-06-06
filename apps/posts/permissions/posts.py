"""Post Permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsPostOwner(BasePermission):
    """Is Post Owner."""

    def has_object_permission(self, requet, view, obj):
        """Only allow access to post owner."""
        return requet.user == obj.user
