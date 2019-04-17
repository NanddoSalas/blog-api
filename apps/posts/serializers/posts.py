"""Post Serializers."""

# Django REST Framework
from rest_framework import serializers

# Models
from apps.posts.models import Post


class PostModelSerializer(serializers.ModelSerializer):
    """Post Model Serializer."""

    user = serializers.StringRelatedField()

    class Meta:
        """Meta Options."""

        model = Post
        
        fields = '__all__'

        read_only_fields = (
            'id',
            'created',
            'updated',
            'user',
        )

    def create(self, data):
        """Handdle post creation.
        
        User is taken from serializer context.
        """
        user = self.context['request'].user
        return Post.objects.create(user=user, **data)