from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .forms import SignupForm
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
class UserSignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/auth_form.html'
    success_url = reverse_lazy('LoginPage')

    def form_valid(self, form):
        messages.success(self.request, f'Account { form.cleaned_data['username'] } is Created Successfully. Please LogIn!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'SignUp'
        return context
        

class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'accounts/auth_form.html'

    def get_success_url(self):
        return reverse_lazy('ProfilePage')
    
    def form_valid(self, form):
        messages.success(self.request, "Logged In Succesfully !")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'LogIn'
        return context
    

class UserLogoutView(LogoutView):
    def get_success_url(self):
        messages.success(self.request, "LogOut Successfully !")
        return reverse_lazy('LoginPage')
    

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'