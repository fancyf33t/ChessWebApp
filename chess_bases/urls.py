"""Defines URL patterns for chess_bases"""

from django.urls import path 

from . import views 

app_name = 'chess_bases'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics Page
    path('topics/', views.topics, name='topics'),
    # Single topic details
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # page for adding topics
    path('new_topic/', views.new_topic, name='new_topic'),
    # page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]