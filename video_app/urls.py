from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login_user/',views.login_user,name='login_user'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('meeting/', views.videocall, name='meeting'),
    path('logout/', views.logout_user, name='logout'),
    path('join_room/', views.join_room, name='join_room'),
]