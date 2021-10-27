from django.urls import path
from .views import workout_page, new_workout, update_workout

urlpatterns = [
    path('', workout_page, name='w_page'),
    path('new', new_workout, name='w_new'),
    path('update', update_workout, name='w_update')
]
