from django.urls import path
from .views import index, edit_profile

urlpatterns = [
    path('', index, name = 'index'),
    path('edit', edit_profile, name = 'edit_profile'),
]