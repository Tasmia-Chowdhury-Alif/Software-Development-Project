from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name= 'RegistrationPage'),
    path('login/', views.UserLoginView.as_view(), name= 'LoginPage'),
    path('logout/', views.UserLogoutView.as_view(), name= 'LogoutPage'),
    path('profile/', views.UserProfileUpdateView.as_view(), name= 'ProfilePage'),
]