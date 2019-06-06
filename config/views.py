"""Handler and Other Views."""

# Django
from django.http import JsonResponse

# Django REST Framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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


@api_view(['GET'])
def api_root(request):
    """Show all Api links."""
    return Response({
        'signup': '/users/signup/',
        'login': '/users/login/',
        'verify': '/users/verify/',
        'user': '/users/{username}/',
        'posts': '/posts/',
        'post': '/posts/{post_id}/',
        'comments': '/posts/{post_id}/comments/',
        'comment': '/posts/{post_id}/comments/{comment_id}/'
    })
