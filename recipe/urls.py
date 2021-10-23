from django.urls import path
from .views import recipe_page
from .views import recipe_detail_bruschetta
urlpatterns = [
    path('', recipe_page),
    path('recipe-bruschetta', recipe_detail_bruschetta)
]