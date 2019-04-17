"""Post urls."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from apps.posts.views import PostViewSet


router = DefaultRouter()

router.register(
    r'posts',
    PostViewSet,
    basename='posts'
)

urlpatterns = [
    path('', include(router.urls))
]