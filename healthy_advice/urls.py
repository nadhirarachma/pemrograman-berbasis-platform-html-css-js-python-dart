from django.urls import path
from healthy_advice.views import healthy_advice

urlpatterns = [
    path('', healthy_advice, name="healthy-advice"),
]