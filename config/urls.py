"""Urls main module."""

# Django
from django.urls import path, include
from django.conf import settings

# Views
from config.views import Handler403, Handler404


urlpatterns = [
    path('', include('apps.users.urls')),
    path('', include('apps.posts.urls')),
]

# Handdle Errors

handler400 = 'rest_framework.exceptions.bad_request'
handler403 = Handler403
handler404 = Handler404
handler500 = 'rest_framework.exceptions.server_error'