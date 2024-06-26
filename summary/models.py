from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    gender = models.CharField(max_length = 30, default='')
    age = models.CharField(max_length = 30, default='')
    profession = models.CharField(max_length = 30, default='')
    mobile = models.CharField(max_length = 30, default='')
    address = models.CharField(max_length = 30, default='')

