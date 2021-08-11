"""helloworldchat URL Configuration

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
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pages.views import get_homepage_view
from accounts.views import registerPageView, loginPageView, logoutUser, userProfileView, userProfileEdit
from chat.views import  chatMessageView
urlpatterns = [
    path('', get_homepage_view, name='home'),
    path('register/', registerPageView, name='register'),
    path('userprofile/', userProfileView, name='userprofile'),
    path('chat/', chatMessageView, name='chat'),
    path('userprofile/edit/', userProfileEdit, name='edit'),
    path('logout/', logoutUser, name='logout'),
    path('login/', loginPageView, name='login'),   
    path('admin/', admin.site.urls, name='admin'),
]
urlpatterns += staticfiles_urlpatterns()
