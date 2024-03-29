"""Post urls."""

# Django REST Framework
from rest_framework.routers import SimpleRouter

# Views
from apps.posts.views import (
    PostViewSet,
    CommentViewSet
)


router = SimpleRouter()

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
