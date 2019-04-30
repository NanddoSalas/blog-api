"""Post Tests."""

# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Models
from apps.users.models import User
from rest_framework.authtoken.models import Token


class PostTestCase(APITestCase):
    """Post Test Case."""

    def setUp(self):
        """setUp method."""

        # Create users for be used in the posts testing

        self.user1 = User.objects.create_user(
            username='test1',
            email='test1@localhost',
            password='P455w0rd'
        )

        self.user2 = User.objects.create_user(
            username='test2',
            email='test2@localhost',
            password='P455w0rd'
        )

        Token.objects.create(user=self.user1)
        Token.objects.create(user=self.user2)

        self.posts_url = '/posts/'

    def test_creation(self):
        """Test post's creation."""
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(self.user1.auth_token.key)
        )
        response = self.client.post(
            path=self.posts_url,
            data={
                'title': 'Post 1',
                'text': 'Test 1'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)