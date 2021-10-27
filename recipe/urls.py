from django.urls import path
from .views import recipe_page
from .views import recipe_detail_bruschetta
from .views import recipe_detail_shrimp
urlpatterns = [
    path('', recipe_page),
    path('bruschetta/', recipe_detail_bruschetta),
    path('honey-walnut-shrimp/', recipe_detail_shrimp),
]