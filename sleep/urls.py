from django.urls import path
from .views import mainpage_sleep, new_sleep, update_sleep

urlpatterns = [
    path('', mainpage_sleep, name='mainpage_s'),
    path('new', new_sleep, name='new_s'),
    path('update', update_sleep, name='update_s')
]
