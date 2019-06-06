"""
Settings file for runing tests faster.
"""

from .base import * # noqa
from .base import env


# Base
DEBUG = False
SECRET_KEY = env("DJANGO_SECRET_KEY", default="7lEaACt4wsCj8JbXYgQLf4BmdG5QbuHTMYUGir2Gc1GHqqb2Pv8w9iXwwlIIviI2")
TEST_RUNNER = "django.test.runner.DiscoverRunner"


# Cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": ""
    }
}


# Passwords
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]


# Email
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

# Celery
CELERY_TASK_ALWAYS_EAGER = True  # Tasks will be executed locally
