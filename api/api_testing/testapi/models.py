from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    phone_number = models.BigIntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=15)