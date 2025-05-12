from django.urls import path
from .views import home, signup, user_login, user_logout, profile, pass_change, pass_change2

urlpatterns = [
    path('', home, name='homepage'),
    path('signup/', signup, name='signuppage'),
    path('login/', user_login, name='loginpage'),
    path('logout/', user_logout, name='logoutpage'),
    path('profile/', profile, name='profilepage'),
    path('pass_change/', pass_change, name='passchangepage'),
    path('pass_change2/', pass_change2, name='passchang2epage'),
]