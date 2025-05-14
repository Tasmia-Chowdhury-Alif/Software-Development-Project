from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name= 'RegisterPage'),
    path('login/', views.user_login, name= 'LoginPage'),
    path('profile/', views.profile, name= 'ProfilePage'),
    path('profile/pass_change', views.pass_change, name= 'PassChangePage'),
]