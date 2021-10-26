from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length = 30) 
    gender = models.CharField(max_length = 30)
    age = models.CharField(max_length = 30)
    profession = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    mobile = models.CharField(max_length = 30)
    address = models.CharField(max_length = 30)

