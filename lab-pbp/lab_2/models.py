from django.db import models

# Create your models here.

class Note(models.Model):
    to = models.CharField(max_length = 30)
    fromm = models.CharField(max_length = 30)
    title = models.CharField(max_length = 30)
    message = models.CharField(max_length = 100)