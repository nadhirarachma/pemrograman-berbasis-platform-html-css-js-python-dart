from django.db import models
from django.db.models.fields import TextField

class News(models.Model):
    title = models.CharField(max_length=30)
    thumbnail = models.CharField(max_length=50)
    slug = models.SlugField()
    intro = models.TextField()
    # image= models.CharField(max_length=500)
    news = models.TextField()

class FeedBack(models.Model):
    name = models.CharField(max_length=30)
    the_feedback = models.TextField()

  
