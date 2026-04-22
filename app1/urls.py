from django.urls import path
from . import views
url patterns = [
    path('hello/', views.hello_world, name='hello_world'),
      path('add/', views.add_numbers, name='add_numbers'),
]