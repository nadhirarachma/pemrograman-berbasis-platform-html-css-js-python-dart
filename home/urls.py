from django.urls import path
from django.conf.urls import url

from .views import index, news_page, feedback

#
# localhost/home/profile/editprofile
#
#
#
#

urlpatterns = [
    path('', index, name='index'), 
    path('feedback', feedback, name='feedback' ),
    path('<str:slug>/', news_page, name='readmore'),
    
    
]