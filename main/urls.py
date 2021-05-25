from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties', views.properties, name='properties'),
    path('property_details', views.property_details, name='property_details'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register_success', views.register_success, name='register_success'),
]