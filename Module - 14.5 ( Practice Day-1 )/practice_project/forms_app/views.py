from django.shortcuts import render
from . import forms 

# Create your views here.
def home(request):
    api_form = forms.ApiForm()
    model_form_var = forms.Model_Form()
    return render(request, 'home.html', context={'api_form' : api_form , 'model_form' : model_form_var })