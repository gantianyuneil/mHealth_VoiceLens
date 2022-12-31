from django.db import models

# Create your models here.
class userInfo(models.Model):
    # username and password length are based on UBIT standards.
    id = models.CharField(primary_key=True, max_length=32)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=32)
