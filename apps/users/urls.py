"""users urls module."""

# Django REST Framework
from rest_framework.routers import SimpleRouter

# Views
from apps.users.views import UserViewSet


router = SimpleRouter()

router.register(
    r'users',
    UserViewSet,
    basename='users'
)

urlpatterns = router.urls
