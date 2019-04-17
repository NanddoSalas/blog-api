"""Post models."""

# Django
from django.db import models


class Post(models.Model):
    """Post Model."""

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=60)
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return Title."""
        return self.title