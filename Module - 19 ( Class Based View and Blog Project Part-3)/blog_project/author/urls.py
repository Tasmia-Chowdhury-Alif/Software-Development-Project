from django.urls import path, include
from . import views
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name= 'RegisterPage'),
    # path('login/', views.user_login, name= 'LoginPage'),
    path('login/', views.UserLoginView.as_view(), name= 'LoginPage'),
    # path('logout/', views.user_logout, name= 'LogoutPage'),
    path('logout/', views.UserLogoutView.as_view(), name= 'LogoutPage'),
    path('profile/', views.profile, name= 'ProfilePage'),
    path('profile/edit/', views.edit_profile, name= 'EditProfilePage'),
    path('profile/edit/pass_change', views.pass_change, name= 'PassChangePage'),
]