from django.db import models
import mysql.connector as sql
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    address = models.TextField(max_length=255)
    city = models.CharField(max_length=255)
    grade = models.IntegerField()
    section = models.CharField(max_length=10)