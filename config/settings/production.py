"""
Settings file for production.
"""

from .base import * # noqa
from .base import env

# Base

DEBUG = False
SECRET_KEY = env('DJANGO_SECRET_KEY', default='8u(dh#bi+^j@(w0b-c5f6c0&nfhd4h*(qz-pgve+$=nmk-m)9&')
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS')  # (FOO=a,b,c)

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

# Email

EMAIL_BACKEND = "anymail.backends.sendgrid.EmailBackend"

ANYMAIL = {
    "SENDGRID_API_KEY": env('ANYMAIL_API_KEY'),
}

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
