from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('properties', views.properties, name='properties'),
    path('property/property_details/<int:property_id>/', views.property_details, name='property_details'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register_success', views.register_success, name='register_success'),
    path('add_property', views.add_property, name='add_property'),
    path('my_properties', views.my_properties, name='my_properties'),
    path('review', views.review, name='review'),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/blog_details/<int:blog_id>/', views.blog_details, name='blog_details'), 
    path('all_agents', views.all_agents, name='all_agents'),
    path('faqs', views.faqs, name='faqs'),
    path('my_profile', views.my_profile, name='my_profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('contact', views.contact, name='contact'),
    path('for_rent', views.for_rent, name='for_rent'),
    path('for_sale', views.for_sale, name='for_sale'),
    path('property_search', views.property_search, name='property_search'),
]