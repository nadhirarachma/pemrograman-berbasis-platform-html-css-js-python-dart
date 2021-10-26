from django.urls import path
from healthy_advice.views import healthy_advice, manfaat_istirahat, get_all_comment, delete_comment
urlpatterns = [
    path('', healthy_advice, name="healthy-advice"),
    path('manfaat_istirahat', manfaat_istirahat, name="manfaat-istirahat" ), 
    path('get_all_comment', get_all_comment, name='get-all-comment'),
    path('delete/<int:id>', delete_comment, name='delete-comment'),
]