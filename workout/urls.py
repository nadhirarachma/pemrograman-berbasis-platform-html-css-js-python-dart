from django.urls import path
from .views import workout_page, new_workout, update_workout, reset_workout

urlpatterns = [
    path('', workout_page, name='w_page'),
    path('update', update_workout, name='w_update'),
    path('reset', reset_workout, name='w_reset')
]
