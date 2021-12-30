from django.urls import path
from .views import summary, edit_profile, get_profile, post_profile

urlpatterns = [
    path('', summary, name = 'summary'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
    path('get_profile/', get_profile, name = 'get_profile'),
    path('post_profile/', post_profile, name = 'post_profile'),
]