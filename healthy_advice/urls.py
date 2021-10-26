from django.urls import path
from healthy_advice.views import healthy_advice, manfaat_istirahat
urlpatterns = [
    path('', healthy_advice, name="healthy-advice"),
    path('manfaat_istirahat', manfaat_istirahat, name="manfaat-istirahat" )
]