"""Post Filters."""

# Filters
from django_filters import rest_framework as filter

# Models
from apps.posts.models import Post


class PostFilter(filter.FilterSet):
    """Filter by post's creator (username)."""

    username = filter.CharFilter(field_name='user', lookup_expr='username')

    class Meta:
        """Meta Options."""

        model = Post
        fields = ('user',)
