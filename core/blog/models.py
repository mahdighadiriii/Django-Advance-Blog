from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

'''
this is a class to define posts for blog app
'''

# getting user model object
User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey('category', on_delete=models.SET_NULL, null=True)

    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    published_date = models.DateField()

    def __str__(self):
        return self.title
    
    def get_snippet(self):
        return self.content[0:10]
    
    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
