from django.test import TestCase
from django.urls import reverse, resolve
from ..views import IndexView,PostCreateView


class TestUrl(TestCase):
    
        
    def test_blog_create_url_resolve(self):
        url = reverse('blog:post-create')
        self.assertEquals(resolve(url).func.view_class,PostCreateView)