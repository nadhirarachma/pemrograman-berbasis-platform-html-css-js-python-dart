from django.urls import path
from .views import summary, edit_profile

urlpatterns = [
    path('', edit_profile, name = 'edit_profile'),
    path('activity/', summary, name = 'summary'),
]