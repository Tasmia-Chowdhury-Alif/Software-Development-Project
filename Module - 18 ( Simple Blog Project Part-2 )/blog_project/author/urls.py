from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name= 'RegisterPage'),
    path('login/', views.user_login, name= 'LoginPage'),
    path('logout/', views.user_logout, name= 'LogoutPage'),
    path('profile/', views.profile, name= 'ProfilePage'),
    path('profile/edit/', views.edit_profile, name= 'EditProfilePage'),
    path('profile/edit/pass_change', views.pass_change, name= 'PassChangePage'),
]