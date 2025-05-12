from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms 

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': ''}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': ''}))
    email = forms.EmailField(required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']