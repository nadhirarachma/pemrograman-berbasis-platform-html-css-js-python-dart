from django.urls import path
from .views import recipe_detail_salmon, recipe_page
from .views import recipe_detail_bruschetta
from .views import recipe_detail_shrimp
from .views  import recipe_detail_salad
from .views import recipe_detail_greek_chicken
# from .views import post_detail


urlpatterns = [
    path('', recipe_page),
    path('bruschetta/', recipe_detail_bruschetta),
    path('honey-walnut-shrimp/', recipe_detail_shrimp),
    path('salad-caprese-zoodles/', recipe_detail_salad),
    path('garlicky-greek-chicken/', recipe_detail_greek_chicken),
    path('salmon-panggang/', recipe_detail_salmon),
    # path('<slug:slug>/', post_detail, name='post_detail'),
]


