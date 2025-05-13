from django.shortcuts import render, redirect
from . import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

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
            return redirect('RegisterPage')
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'author/register.html', context={'form' : register_form})

def user_login(request):
    form = UserCreationForm()
    pass