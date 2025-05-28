from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name= 'SignupPage'),
    path('login/', views.UserLoginView.as_view(), name= 'LoginPage'),
    path('logout/', views.UserLogoutView.as_view(), name= 'LogoutPage'),
]