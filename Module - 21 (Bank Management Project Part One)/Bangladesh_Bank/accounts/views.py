from django.shortcuts import render
from .forms import UserRegistrationForm
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy

# Create your views here.
class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'accounts/user_registration.html'
    success_url = reverse_lazy('RegistrationPage')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('HomePage')
    
class UserLogoutView(LogoutView):
    next_page = reverse_lazy('LoginPage')