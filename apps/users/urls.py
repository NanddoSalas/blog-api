"""users urls module."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from apps.users.views import UserViewSet


router = DefaultRouter()

router.register(
    r'users',
    UserViewSet,
    basename='users'
)

urlpatterns = [
    path('', include(router.urls)),
]