from django.urls import path
from .views import mainpage_sleep, new_sleep, update_sleep, reset_sleep, get_sleep, get_sleeps, reset_sleeps, post_sleeps

urlpatterns = [
    path('', mainpage_sleep, name='mainpage_s'),
    path('new', new_sleep, name='new_s'),
    path('update', update_sleep, name='update_s'),
    path('reset', reset_sleep, name='reset_s'),
    
    path('get_sleep', get_sleep, name='get-sleep'),

    path('get_sleeps', get_sleeps, name='get-sleeps'),
    path('reset_sleeps', reset_sleeps, name='reset-sleeps'),
    path('post_sleeps', post_sleeps, name='post-sleeps'),
]
