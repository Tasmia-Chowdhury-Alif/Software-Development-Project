from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name= 'homepage'),
    path('about/', views.about, name= 'aboutpage'),
    path('submit_form/', views.submit_form, name= 'submit_form'),
    path('django_form/', views.passward_form, name= 'django_form'),
]