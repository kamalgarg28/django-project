from django.db import models
import mysql.connector as sql
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username=None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


