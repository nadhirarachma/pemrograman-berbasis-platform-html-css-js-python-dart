from django.urls import path
from .views import recipe_detail_bruschetta , recipe_detail_salmon ,recipe_detail_shrimp, recipe_detail_greek_chicken, recipe_detail_salad,recipe_detail_chicken_soup
from .views import recipe_page, delete_comment, edit_comment, get_all_comment
urlpatterns = [
    path('', recipe_page),
    path('bruschetta/', recipe_detail_bruschetta),
    path('honey-walnut-shrimp/', recipe_detail_shrimp),
    path('salad-caprese-zoodles/', recipe_detail_salad),
    path('garlicky-greek-chicken/', recipe_detail_greek_chicken),
    path('baked-salmon/', recipe_detail_salmon),
    path('chicken-soup/', recipe_detail_chicken_soup),
    path('delete/<int:id>', delete_comment, name='delete-comment'),
    path('edit/<int:id>', edit_comment, name='edit-comment'),
    path('get_all_comment', get_all_comment, name='get-all-comment'),

]


