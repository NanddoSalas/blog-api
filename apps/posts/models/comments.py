"""Comment Models."""

# Django
from django.db import models


class Comment(models.Model):
    """Comment Model."""

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE
    )

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return @{username} at #{title}."""
        return '@{} at #{}'.format(
            self.user.username,
            self.post.title
        )
