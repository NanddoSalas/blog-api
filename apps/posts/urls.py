"""Post urls."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from apps.posts.views import (
    PostViewSet,
    CommentViewSet
)


router = DefaultRouter()

router.register(
    r'posts',
    PostViewSet,
    basename='posts'
)

router.register(
    r'posts/(?P<id>[0-9]+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = router.urls