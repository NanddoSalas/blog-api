"""Urls main module."""

# Django
from django.urls import path
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
]