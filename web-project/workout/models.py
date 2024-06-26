from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Exercise(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    today = models.DateField(default=datetime.date.today)
    time = models.IntegerField(default=0)
