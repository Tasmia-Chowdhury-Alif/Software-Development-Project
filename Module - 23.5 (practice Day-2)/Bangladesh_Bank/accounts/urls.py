from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name= 'registration'),
    path('login/', views.UserLoginView.as_view(), name= 'login'),
    path('logout/', views.UserLogoutView.as_view(), name= 'logout'),
    path('profile/', views.UserProfileUpdateView.as_view(), name= 'profile'),
    path('change_password/', views.UserPasswordChangeView.as_view(), name= 'password-change')
]