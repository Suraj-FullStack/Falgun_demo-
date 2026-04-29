from django.urls import path, include
from .views import categoryGenericview, categoryDetailGenericview, tableGenericview

urlpatterns = [
    path('category/', categoryGenericview.as_view()),
    path('category/<int:id>/', categoryDetailGenericview.as_view()),
    path('table/', tableGenericview.as_view()),
]
