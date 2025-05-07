from django.urls import path, include 
from .views import add_meal  

urlpatterns = [
    path('add_meal/', add_meal, name='add_meals',),
]