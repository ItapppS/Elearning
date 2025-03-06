from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('otto/', views.otto, name='otto'),
    path('bionic_hand/', views.bionic_hand, name='bionic_hand'),
    path('humanoid_robot/', views.humanoid_robot, name='humanoid_robot'),
    path('home_automation/', views.home_automation, name='home_automation'),
    path('solar-tracking/', views.solar_tracking, name='solar-tracking'),
    path('obstraction_avoiding_car/', views.obstraction_avoiding_car, name='obstraction_avoiding_car'),
    path('robotics/', views.robotics, name='robotics'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('base/', views.base, name='base'),
    path('demo/', views.demo, name='demo'),
    path('bionic_hand/', views.bionic_hand, name='bionic_hand'),
    path('solar_tracking/', views.solar_tracking, name='solar_tracking'),
    path('asterbot/', views.asterbot, name='asterbot'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('doghead/', views.doghead, name = 'doghead'),
    path('realtimeclock/', views.realtimeclock, name = 'realtimeclock'),    
   
   path('navbarr/', views.navbarr, name='navbarr'),
   path('verify_email/', views.verify_email, name='verify_email'),
   path('NA/', views.NA, name='NA'),
    path('technology/<slug:slug>/', views.technology_detail, name='technology_detail'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
   ]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



