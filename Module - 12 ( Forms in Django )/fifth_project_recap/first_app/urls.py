from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name= 'homepage'),
    path('about/', views.about, name= 'aboutpage'),
    path('submit_form/', views.submint_form, name= 'submit_form'),
]