"""
URL configuration for Practice_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from authentication_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'HomePage'),
    path('signup/', views.user_signup, name= 'SignupPage'),
    path('login/', views.user_login, name= 'LoginPage'),
    path('logout/', views.user_logout,name= 'LogoutPage'),
    path('profile/', views.profile, name= 'ProfilePage'),
    path('change_password/', views.change_pass, name= 'ChangePassPage'),
    path('change_password2/', views.change_pass2, name= 'ChangePassWithoutPage'),
    
]
