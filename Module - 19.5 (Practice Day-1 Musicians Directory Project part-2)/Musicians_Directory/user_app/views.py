from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from . import forms 
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class UserSignupView(CreateView):
    form_class = forms.SignupForm
    template_name = 'user_app/login.html'
    success_url = reverse_lazy('LoginPage')

    def form_valid(self, form):
        messages.success(self.request, 'Account Created Successfully! Please Login')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['type'] = 'User SignUp'
        return context

class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user_app/login.html'
    # success_url = reverse_lazy('HomePage') # it Doesn't work for LoginView 

    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['type'] = 'LogIn'
        return context
    
    def get_success_url(self):
        return reverse_lazy('HomePage')
    