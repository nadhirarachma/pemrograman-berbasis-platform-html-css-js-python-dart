from django.urls import path
from .views import index, add_friend

urlpatterns = [
    path('', index, name = 'index'),
    path('add', add_friend, name = 'add_friend')
]
