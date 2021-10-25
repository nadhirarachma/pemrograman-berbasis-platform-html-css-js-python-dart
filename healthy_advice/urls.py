from django.urls import path
from healthy_advice.views import healthy_advice, rate_anu
urlpatterns = [
    path('', healthy_advice, name="healthy-advice"),
    path('rate_anu', rate_anu, name="rate-view" )
]