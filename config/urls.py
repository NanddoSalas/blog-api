"""Urls main module."""

# Django
from django.urls import path, include

# Views
from config.views import Handler403, Handler404, api_root


urlpatterns = [
    path('', api_root),
    path('', include('apps.users.urls')),
    path('', include('apps.posts.urls')),
]

# Handdle Errors

handler400 = 'rest_framework.exceptions.bad_request'
handler403 = Handler403
handler404 = Handler404
handler500 = 'rest_framework.exceptions.server_error'
