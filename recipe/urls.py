from django.urls import path
from .views import recipe_page
from .views import recipe_detail_bruschetta
from .views import recipe_detail_shrimp
from .views  import recipe_detail_salad
from .views import recipe_detail_greek_chicken
urlpatterns = [
    path('', recipe_page),
    path('bruschetta/', recipe_detail_bruschetta),
    path('honey-walnut-shrimp/', recipe_detail_shrimp),
    path('salad-caprese-zoodles/', recipe_detail_salad),
    path('garlicky-greek-chicken/', recipe_detail_greek_chicken),
]