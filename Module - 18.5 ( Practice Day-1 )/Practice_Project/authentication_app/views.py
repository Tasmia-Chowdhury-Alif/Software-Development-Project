from django.shortcuts import render, redirect 
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user_signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have Signed Up Successfully')
            return redirect('LoginPage')
    return render(request, 'authentication_app/signup.html', context={'form' : form, 'type' : 'SignUp'})

def user_login(request):
    # form = forms.UserLoginForm(request= request.user)
    form = AuthenticationForm()
    if request.method == 'POST':
        # form = forms.UserLoginForm(request= request.user, data= request.POST)
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(request, username= user_name, password= user_password)
            if user != None :
                login(request, user)
                messages.success(request, "Logged In Successfully")
                return redirect('ProfilePage')
    
    return render(request, 'authentication_app/signup.html', context={'form' : form, 'type' : 'LogIn'})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('HomePage')

@login_required
def profile(request):
    return render(request, 'authentication_app/profile.html')

@login_required
def change_pass(request):
    form = PasswordChangeForm(user= request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Password has been Changed Successfully')
            return redirect('ProfilePage')
    return render(request, 'authentication_app/pass_change.html', context={'form' : form})

@login_required
def change_pass2(request):
    form = SetPasswordForm(request.user)
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Password has been Changed Successfully')
            return redirect('ProfilePage')
    return render(request, 'authentication_app/pass_change.html', context={'form' : form})

