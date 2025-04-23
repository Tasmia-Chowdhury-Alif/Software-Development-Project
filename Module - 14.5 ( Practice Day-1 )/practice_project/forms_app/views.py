from django.shortcuts import render
from . import forms 

# Create your views here.
def home(request):
    api_form = forms.ApiForm()
    return render(request, 'home.html', context={'api_form' : api_form})