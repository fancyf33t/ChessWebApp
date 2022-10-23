"""Defines URL patterns for users"""

from django.urls import path, include 

from . import views 

app_name = 'users'
urlpatterns=[
    # default authentification
    path('', include('django.contrib.auth.urls')),
    # Registration
    path('register/', views.register, name='register'),
]