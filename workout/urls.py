from django.urls import path
from .views import workout_page, update_workout, reset_workout, get_exercise, post_exercise

urlpatterns = [
    path('', workout_page, name='w_page'),
    path('get', get_exercise, name='w_get'),
    path('post', post_exercise, name='w_post'),
    path('update', update_workout, name='w_update'),
    path('reset', reset_workout, name='w_reset')
]
