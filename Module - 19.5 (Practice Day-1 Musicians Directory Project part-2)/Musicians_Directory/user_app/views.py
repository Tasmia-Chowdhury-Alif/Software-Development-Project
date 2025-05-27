from django.shortcuts import render
from django.contrib.auth.views import LoginView
from . import forms 

# Create your views here.
class UserLoginView(LoginView):
    form_class = forms.UserLoginForm
    template_name = 'user_app/login.html'