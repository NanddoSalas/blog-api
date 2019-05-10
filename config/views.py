"""Handler and Other Views."""

# Django
from django.http import JsonResponse

# Django REST Framework
from rest_framework import status


def Handler403(request, exception):
    """
    Generic 403 error handler.
    """
    data = {
        'error': 'Forbidden (403)'
    }
    return JsonResponse(data=data, status=status.HTTP_403_FORBIDDEN)


def Handler404(request, exception):
    """
    Generic 404 error handler.
    """
    data = {
        'error': 'Not Found (404)',
    }
    return JsonResponse(data=data, status=status.HTTP_404_NOT_FOUND)