"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from board import views

app_name='board'

urlpatterns = [
    # path('create', views.post_create), #User에 관한 API를 처리하는 view로 Request를 넘김
    path('', views.PostView.as_view(), name="list"),
    path('<int:post_id>', views.PostView.as_view(), name="post") #User pk id가 전달되는 경우

    #path('login', views.login, name='login'),
    #path('signup', views.signup, name='signup'),
    #path('logout', views.logout, name='logout'),
]
