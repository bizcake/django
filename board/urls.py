from django.urls import path
from board import views

app_name = "board"

urlpatterns = [
    path('', views.index, name='list'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
]