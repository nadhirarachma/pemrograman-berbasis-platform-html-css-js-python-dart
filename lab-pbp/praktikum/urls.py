"""pbp2021 URL Configuration

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
from django.urls import path, re_path
from django.contrib import admin
from django.urls.conf import include
from lab_1.views import index as index_lab1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lab-1/', include('lab_1.urls')),
    path('lab-2/', include('lab_2.urls')),
    path('lab-3/', include('lab_3.urls')),
    path('lab-4/', include ('lab_4.urls')),
    path('lab-5/', include ('lab_5.urls')),
    re_path(r'^$', index_lab1, name = 'index')
]
