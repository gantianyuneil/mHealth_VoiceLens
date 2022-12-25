from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    # maximum length of a username is 12
    username = models.CharField(max_length=12)
    pwd = models.CharField(max_length=20)
