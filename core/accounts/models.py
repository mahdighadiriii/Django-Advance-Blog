from django.db import models
from django.contrib.auth import (BaseUserManager, AbstractBaseUser, PermissionMixin)
from django.utils.translation import ungettext_lazy as _
# Create your models here.


class UserManager(BaseUserManager):
    """
    custom user model manager where email is the unique identifiers for authentication instead usernames.
    """

    def created_user(self,email,password,**extra_fields):
        """
        created and save a User with the given email and password
        """
        if not email:
            raise ValueError(_("the email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        """
        create and save a SuperUser with the given email and password
        """
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('superuser must have is_superuser=True.'))
        return self.create_user(email,password,**extra_fields)




class User(AbstractBaseUser,PermissionMixin):
    """
    custom User Model for our app
    """
    email = models.EmailField(max_length=250,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    #is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    REQUIRED_FIELDS = []

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DurationField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email
    
