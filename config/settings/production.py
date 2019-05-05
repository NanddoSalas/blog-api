"""
Settings file for production.
"""

from .base import *

# Base

DEBUG = False
SECRET_KEY = env('DJANGO_SECRET_KEY', default='8u(dh#bi+^j@(w0b-c5f6c0&nfhd4h*(qz-pgve+$=nmk-m)9&')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS') # (FOO=a,b,c)

# Databases

DATABASES = {
    'default': env.db('DATABASE_URL'),
}

# Caches

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')