from django.urls import path
from healthy_advice.views import healthy_advice, get_all_comment, delete_comment, edit_comment, detail_article, get_all_article,post_comment_api, edit_comment_api
urlpatterns = [
    path('', healthy_advice, name="healthy-advice"),
    path('get_all_comment', get_all_comment, name='get-all-comment'),
    path('delete/<int:id>', delete_comment, name='delete-comment'),
    path('edit/<int:id>', edit_comment, name='edit-comment'),
    path('details/<int:id>', detail_article, name='detail-article'),
    path('get_all_article', get_all_article, name='get-all-article'),
    path('addAPI', post_comment_api, name='post-comment-api'),
    path('editCommentAPI/<int:id>', edit_comment_api, name='edit-comment-api'),
]