from django.shortcuts import render, redirect
from . import forms 

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('HomePage')
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', context={'form' : task_form})

def edit_task(request):
    pass

def delete_task(request):
    pass

def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('HomePage')
    else:
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', context={'form' : category_form})

def edit_category(request):
    pass

def delete_category(request):
    pass