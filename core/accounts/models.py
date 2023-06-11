from django.db import models
from django.contrib.auth import (BaseUserManager, AbstractBaseUser, PermissionMixin)
# Create your models here.



class User(AbstractBaseUser,PermissionMixin):
    email = models.EmailField(max_length=250,unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DurationField(auto_now=True)


    def __str__(self):
        return self.email