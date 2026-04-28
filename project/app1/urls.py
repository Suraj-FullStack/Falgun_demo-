from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.category, name='category'),
    path('category/<int:id>/', views.category_list, name='category_detail'),
   
]
