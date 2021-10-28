from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# class Rating(models.Model):
#     score = models.IntegerField(default=0,
#         validators=[
#             MaxValueValidator(5),
#             MinValueValidator(0),
#         ]
#     )
#     def __str__(self):
#         return str(self.pk)
# class Product(models.Model):
#     # image = models.ImageField(null=False, blank=False)
#     name = models.CharField(max_length=100, null=False, blank=False)


class CommentHealthy(models.Model):
    commentator_name = models.CharField(default="",max_length=100, null=True)
    # commentator_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='commentator_name')
    comment_field = models.TextField(default="")


