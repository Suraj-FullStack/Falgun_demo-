from django.urls import path
from .views import *
urlpatterns = [
   path('home/', home),
   path('index/', index),
   path('tasks/', tasks),
   path('tasks/create/', create),
   path('tasks/<id>/', task_update),
   path('tasks/<id>/mark/', mark),
   path('tasks/<id>/delete/', delete),
]