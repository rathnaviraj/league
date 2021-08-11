from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    type = models.CharField(max_length=40)