from django.urls import path
from .views import fill_in_profile, summary, edit_profile

urlpatterns = [
    path('', fill_in_profile, name = 'fill_in_profile'),
    path('activity', summary, name = 'summary'),
    path('edit', edit_profile, name = 'edit_profile'),
]