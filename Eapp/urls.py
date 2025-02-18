from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('otto/', views.otto, name='otto'),
    path('robotics/', views.robotics, name='robotics'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
]