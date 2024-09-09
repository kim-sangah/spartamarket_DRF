from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=10)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=(('F','Female'),('M','Male')), blank=True, null=True)
    introduction = models.TextField(max_length=150, blank=True, null=True)