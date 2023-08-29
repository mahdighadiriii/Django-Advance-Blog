from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime

from accounts.models import User, Profile
from blog.models import Post, Category


class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email="test@test.com", password="a/@1234567"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="test_first_name",
            last_name="test_last_name",
            description="test description",
        )
        self.post = Post.objects.create(
            author=self.profile,
            title="test",
            content="description",
            status=True,
            category=None,
            published_date=datetime.now(),
        )
