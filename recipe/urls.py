from django.urls import path
from .views import recipe_page
urlpatterns = [
    path('', recipe_page),

]