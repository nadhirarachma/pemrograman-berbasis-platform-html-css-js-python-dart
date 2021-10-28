"""nadi URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
import accounts.urls as authentication
import healthy_advice.urls as healthy_advice
import recipe.urls as recipe
import summary.urls as summary
from home.views import index
import home.urls as home
import workout.urls as workout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include(authentication)),
    path('recipe/', include(recipe)),
    path('healthy_advice/', include(healthy_advice)),
    path('summary/', include(summary)),
    path('home/', include(home)),
    path('workout/', include(workout)),
    re_path(r'^$', index, name='index')
]