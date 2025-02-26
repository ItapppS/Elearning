from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('otto/', views.otto, name='otto'),
    path('bionic-hand/', views.bionic_hand, name='bionic-hand'),
    path('humanoid-robot/', views.humanoid_robot, name='humanoid-robot'),
    path('home-automation/', views.home_automation, name='home-automation'),
    path('solar-tracking/', views.solar_tracking, name='solar-tracking'),
    path('obstraction-avoiding-car/', views.obstraction_avoiding_car, name='obstraction-avoiding-car'),
    path('robotics/', views.robotics, name='robotics'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('base/', views.base, name='base'),
    path('demo/', views.demo, name='demo'),
    path('bionic_hand/', views.bionic_hand, name='bionic_hand'),
    path('solar_tracking/', views.solar_tracking, name='solar_tracking'),
    path('asterbot/', views.asterbot, name='asterbot'),
    path('register/', views.register, name='register'),
   
   
   ]