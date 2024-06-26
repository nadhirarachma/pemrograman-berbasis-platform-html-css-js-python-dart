from django.urls import path
from .views import friend_list, index

urlpatterns = [
    path('', index, name='index'),
    # TODO Add friends path using friend_list Views

    path('friends', friend_list, name = 'friend'),
]
