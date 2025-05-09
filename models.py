from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Databse model for users in teh system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    s
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
            """Retrieve full name of user"""
            return self.name
    
    def get_short_name(self):
            """Retrieve short name of user"""
            return self.name
    
    def __str__(self):
            """Return string representation"""
            return self.email