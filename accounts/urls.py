from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	path('login_flutter/' , views.login_flutter, name="login_flutter"),
	path('register_flutter/' , views.register_flutter, name="register_flutter"),
    path('', views.home, name="home"),
]