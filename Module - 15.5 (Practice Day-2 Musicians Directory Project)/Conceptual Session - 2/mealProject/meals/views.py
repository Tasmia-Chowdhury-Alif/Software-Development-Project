from django.shortcuts import render, redirect
from . import models 
from . import forms 

# Create your views here.
def show_meals(request):
    foods = models.Food.objects.all()
    return render(request, 'meals/index.html', context={'foods' : foods})

def add_meal(request):
    form = forms.MealAddForm()
    if request.method == 'POST':
        form = forms.MealAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('meals')
    return render(request, 'meals/meal_add.html', context={'form' : form})