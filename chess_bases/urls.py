"""Defines URL patterns for chess_bases"""

from django.urls import path 

from . import views 

app_name = 'chess_bases'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics Page
    path('topics/', views.topics, name='topics'),
]