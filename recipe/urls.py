from django.urls import path
from .views import postmethod, recipe_detail_bruschetta , recipe_detail_salmon ,recipe_detail_shrimp, recipe_detail_greek_chicken, recipe_detail_salad,recipe_detail_chicken_soup
from .views import recipe_page, delete_comment, get_all_comment
urlpatterns = [
    path('', recipe_page, name ='recipe'),
    path('bruschetta/', recipe_detail_bruschetta, name='recipe-detail-bruschetta'),
    path('honey-walnut-shrimp/', recipe_detail_shrimp, name='recipe-detail-shrimp'),
    path('salad-caprese-zoodles/', recipe_detail_salad, name='recipe-detail-salad'),
    path('garlicky-greek-chicken/', recipe_detail_greek_chicken, name='recipe-detail-greek-chicken'),
    path('baked-salmon/', recipe_detail_salmon, name='recipe-detail-salmon'),
    path('chicken-soup/', recipe_detail_chicken_soup, name='recipe-detail-chicken-soup'),
    path('delete/<int:id>', delete_comment, name='delete-comment'),
    path('get_all_comment', get_all_comment, name='get-all-comment'),
    path('addAPI', postmethod, name='post-method-api'),


]


