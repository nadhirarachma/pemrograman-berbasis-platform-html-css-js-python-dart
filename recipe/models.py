from django.db import models
from datetime import datetime, date

class Comment(models.Model):
    username = models.CharField(default="",max_length=100, null=True)
    content = models.TextField(max_length=160)
    post_date = models.DateField(auto_now_add=True)
