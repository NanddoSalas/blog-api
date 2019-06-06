"""Users Permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Is Account Owner."""

    def has_object_permission(self, request, view, obj):
        """Verify that requesting user is equal than object."""
        return request.user == obj
