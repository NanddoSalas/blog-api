"""
Settings file for the development process.
"""

from .base import *
from .base import env


# General

DEBUG = True

SECRET_KEY = env('DJANGO_SECRET_KEY', default='8u(dh#bi+^j@(w0b-c5f6c0&nfhd4h*(qz-pgve+$=nmk-m)9&')

ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]


# Caches

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}


# Email

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')