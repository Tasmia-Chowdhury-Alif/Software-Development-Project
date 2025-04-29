from django.shortcuts import render, redirect 
from . import forms 

# Create your views here.

def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('HomePage')
    else:
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', context={'form' : category_form})