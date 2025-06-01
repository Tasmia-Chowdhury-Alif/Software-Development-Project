from django.urls import path
from . import views 

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='SignupPage'),
    path('login/', views.UserLoginView.as_view(), name='LoginPage'),
    path('logout/', views.UserLogoutView.as_view(), name='LogoutPage'),
    path('profile/', views.ProfileView.as_view(), name='ProfilePage'),
    path('edit_profile/', views.edit_profile, name='EditProfilePage'),
    path('password/', views.edit_password, name='EditPasswordPage'),
]