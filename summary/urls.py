from django.urls import path
from .views import summary, edit_profile

urlpatterns = [
    path('', summary, name = 'summary'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
]