from django.shortcuts import render, redirect
from .forms import RegistrationForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                # print(form.cleaned_data)
                messages.success(request, 'Account Created Successfully')
                # messages.warning(request, 'Warning message')
                # messages.info(request, 'Info message')
                return redirect('signuppage')

        return render(request, 'signup.html', context={'form' : form})
    else:
        return redirect('profilepage')

def user_login(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()

        if request.method == 'POST':
            form = AuthenticationForm(request=request, data= request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username= name, password= user_password) # checking if the user exists in Database
                if user is not None:
                    login(request, user) # this will make the user to log in to his accoutn
                    return redirect('profilepage') # redirect to the user profile page

        return render(request, 'login.html', context={'form' : form})
    else:
        return redirect('profilepage')
        

def user_logout(request):
    logout(request)
    return redirect('loginpage')
  
# @login_required   # this decorator is used to give access of the view only to authenticated users 
def profile(request):
    if request.user.is_authenticated: # leting only the authenticated user to access the profile page
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)
            if form.is_valid():
                messages.success(request, 'Account Updated Successfully')
                form.save()
                return redirect('profilepage')
        else:
            form = ChangeUserData(instance = request.user)
        return render(request, 'profile.html', context={'form' : form})
    else :
        return redirect('loginpage')
    
def pass_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user= request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user) 
                return redirect('profilepage')
        else:
            form = PasswordChangeForm(user= request.user)
        return render(request, 'passchange.html', context={'form' : form})
    
    else:
        return redirect('loginpage')

def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user= request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user) 
                return redirect('profilepage')
        else:
            form = SetPasswordForm(user= request.user)
        return render(request, 'passchange.html', context={'form' : form})
    
    else:
        return redirect('loginpage')
    
# def change_user_data(request):
#     if not request.user.is_authenticated:
#         form = ChangeUserData()
#         if request.method == 'POST':
#             form = ChangeUserData(request.POST, instance= request.user)
#             if form.is_valid():
#                 form.save()
#                 # print(form.cleaned_data)
#                 messages.success(request, 'Account Updated Successfully')
#                 # messages.warning(request, 'Warning message')
#                 # messages.info(request, 'Info message')
#                 return redirect('profilepage')

#         return render(request, 'profile.html', context={'form' : form})
#     else:
#         return redirect('loginpage')