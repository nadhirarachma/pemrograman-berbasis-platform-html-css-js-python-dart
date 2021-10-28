from django.db import models

class Comment(models.Model):
    username = models.CharField(default="",max_length=100, null=True)
    content = models.TextField(max_length=160)

