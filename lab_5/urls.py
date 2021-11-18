from django.urls import path
from .views import index, postFriend

urlpatterns = [
    path('', index, name = 'index'),
    # path('/notes/<id>', get_note, name = 'get_note'),
    path('post/ajax/friend', postFriend, name = "post_friend"),
    # path('/notes/<id>/update', update_note, name = 'update_note'),
    # path('/notes/<id>/delete', delete_note, name = 'delete_note')
]