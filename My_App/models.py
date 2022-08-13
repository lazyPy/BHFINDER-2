from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200, null=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(verbose_name='Contact Number', max_length=200)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name
