from django.urls import path
from django.conf.urls import url

from .views import index, news_page, feedback, get_all_feedback, get_all_news, post_feedBack


urlpatterns = [
    path('', index, name='index'), 
    path('feedback', feedback, name='feedback' ),
    path('getfeedback', get_all_feedback, name='get-all-feedback'),
    path('getnews', get_all_news, name='get-all-news'),
    path('post_feedback', post_feedBack, name='post_feedback'),
    path('<str:slug>/', news_page, name='readmore'),
    
    
    
]
