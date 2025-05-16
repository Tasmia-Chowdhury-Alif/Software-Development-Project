from django.shortcuts import render, redirect
from . import forms 
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash   
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.RegistrationForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('AddAuthor')
#     else:
#         author_form = forms.RegistrationForm()
#     return render(request, 'author/add_author.html', context={'form' : author_form})

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Registration Successfull")
            return redirect('RegisterPage')
        else:
            messages.warning(request, "Invalid Information !")
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'author/register.html', context={'form' : register_form, 'type' : 'Registration'})

def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(request, username= user_name, password= user_password)
            if user is not None:
                login(request,user)
                messages.success(request, "Login SuccessFully")
                return redirect('ProfilePage')
            else:
                messages.warning(request, "Invalid Login Information !")
    return render(request, 'author/register.html', context={'form' : form, 'type' : 'Login'})

@login_required
def profile(request):
    data = Post.objects.filter(author = request.user)   # for every post filter() checks if 'author' is equal to 'request.user' and shows only the filterd post
    # data = Post.objects.all() 
    return render(request, 'author/profile.html', context={'data' : data})

@login_required
def edit_profile(request):
    form = forms.ChangeUserData(instance= request.user)
    if request.method == 'POST':
        form = forms.ChangeUserData(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated Succefully")
            return redirect('EditProfilePage')
    return render(request, 'author/edit_profile.html', context={'form' : form})

@login_required
def pass_change(request):
    form = PasswordChangeForm(user= request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(user= request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user) # this will create a new session id without logging out the user. this improves user experience
            messages.success(request, "Password Changed Successfully")
            return redirect('ProfilePage')
    return render(request, 'author/pass_change.html', context={'form' : form})

def user_logout(request):
    logout(request)
    return redirect('LoginPage')