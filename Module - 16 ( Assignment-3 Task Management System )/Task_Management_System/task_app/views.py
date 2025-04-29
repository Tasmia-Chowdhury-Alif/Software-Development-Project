from django.shortcuts import render, redirect
from . import models, forms 

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

def edit_task(request, id):
    task_object = models.Task.objects.get(pk= id) # selecting the specific object of task
    task_form = forms.TaskForm(instance= task_object) # using task_object as TaskForm instance

    if request.method == "POST":
        task_form = forms.TaskForm(request.POST, instance= task_object)
        if task_form.is_valid():
            task_form.save()
            return redirect('HomePage')
        
    return render(request, 'add_task.html', context={ 'form' : task_form})
    

def delete_task(request, id):
    task_object = models.Task.objects.get(pk= id)
    task_object.delete()
    return redirect('HomePage')
