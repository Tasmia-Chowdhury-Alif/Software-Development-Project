from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import SignupForm, EditProfileForm
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash


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
        context['submit'] = 'Submit'
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
        context['submit'] = 'Submit'
        return context
    

class UserLogoutView(LoginRequiredMixin, LogoutView):
    def get_success_url(self):
        messages.success(self.request, "LogOut Successfully !")
        return reverse_lazy('LoginPage')
    

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = self.request.user.orders.all()
        context["orders"] = orders
        return context
    

@login_required
def edit_profile(request):
    form = EditProfileForm(instance= request.user)
    if request.method == "POST":
        form = EditProfileForm(data=request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Sucessfully')
            return redirect('ProfilePage')

    return render(request, 'accounts/auth_form.html', context={'form' : form, 'type' : 'Edit Profile', 'submit' : 'Submit'})

@login_required
def edit_password(request):
    form = PasswordChangeForm(user= request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(user= request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Password Changed Sucessfully')
            return redirect('ProfilePage')

    return render(request, 'accounts/auth_form.html', context={'form' : form, 'type' : 'Password Chage your Password', 'submit' : 'Submit'})