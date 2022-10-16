from django.db import connection
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

class User(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,null=False)
    password = models.CharField(max_length=100)
    account_creation_date = models.DateTimeField(default=now,editable=False)

class Teacher(AbstractBaseUser):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    username = models.CharField(max_length=200,null=False)