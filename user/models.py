from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
   username = models.CharField(unique=True, max_length=20, verbose_name="Username", help_text="<br/>Username used to Log-in")
   name = models.TextField(null=False, max_length=30, help_text="<br/>Legal Name") # Legal name of User

   USERNAME_FIELD = 'username'
