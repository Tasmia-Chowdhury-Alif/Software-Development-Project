from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.nav),
    path('more/', views.more),
    path('services/', views.services),
]