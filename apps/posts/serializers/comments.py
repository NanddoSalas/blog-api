"""Comment Serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.posts.models import Comment


class CommentModelSerializer(serializers.ModelSerializer):
    """Comment Model Serializer."""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    commented_by = serializers.StringRelatedField(source='user')

    class Meta:
        """Meta Options."""

        model = Comment

        fields = (
            'id',
            'user',
            'commented_by',
            'text',
            'created',
        )

    def create(self, data):
        """Handdle Comment creation."""
        post = self.context['post']
        return Comment.objects.create(post=post, **data)
