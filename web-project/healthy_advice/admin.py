from django.contrib import admin
from healthy_advice.models import CommentHealthy, HealthyArticle

# Register your models here.
admin.site.register(CommentHealthy)
admin.site.register(HealthyArticle)