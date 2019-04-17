"""Urls main module."""

# Django
from django.urls import path, include
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include('apps.users.urls')),
]