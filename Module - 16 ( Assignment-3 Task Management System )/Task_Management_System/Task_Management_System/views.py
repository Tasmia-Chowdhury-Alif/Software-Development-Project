from django.shortcuts import render, redirect
from task_app import models, forms 

# Create your views here.
def home(request):
    all_tasks = models.Task.objects.all()
    return render(request, 'home.html', context= {'tasks' : all_tasks} )