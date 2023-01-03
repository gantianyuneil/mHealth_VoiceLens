from django.db import models

# Create your models here.
class userInfo(models.Model):
    # username and password length are based on UBIT standards.
    username = models.CharField(primary_key=True, max_length=32)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32, default='x')
    last_name = models.CharField(max_length=32, default='x')
    gender = models.CharField(max_length=32, default='x')
    race = models.CharField(max_length=32, default='x')
    dob = models.CharField(max_length=32, default='x')
    first_language = models.CharField(max_length=32, default='x')
    smoke = models.CharField(max_length=3, default='no')
