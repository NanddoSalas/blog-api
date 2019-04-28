"""Urls main module."""

# Django
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('', include('apps.users.urls')),
    path('', include('apps.posts.urls')),
]