from django.shortcuts import render

# Create your views here.
def show_meals(request):
    return render(request, 'meals/index.html',)