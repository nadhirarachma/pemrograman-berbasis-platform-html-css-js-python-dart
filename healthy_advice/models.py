from django.db import models
from django.contrib.auth.models import User

class CommentHealthy(models.Model):
    commentator_name = models.CharField(default="",max_length=100, null=True)
    comment_field = models.TextField(default="")


class HealthyArticle(models.Model):
    title = models.CharField(max_length=100)
    image_link = models.CharField(max_length=500)
    image_article = models.CharField(max_length=500, default="")
    deskripsi = models.TextField()
    created_at = models.DateField()