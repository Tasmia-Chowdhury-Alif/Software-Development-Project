from django.shortcuts import render
from . forms import *

# Create your views here.

def home(request):
    return render(request, 'first_app/home.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'first_app/about.html', context= {'name' : name, 'email' : email, 'select' : select, })
    
    return render(request, 'first_app/about.html')

def submit_form(request):
    return render(request, 'first_app/form.html')

def Djanog_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)

            print(form.cleaned_data)
    else:
        form = contactForm()

    return render(request, 'first_app/django_form.html', {'form' : form})

def Student_form(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()

    return render(request, 'first_app/django_form.html', {'form' : form})

def Student_form(request):
    if request.method == 'POST':
        form = PasswardValidationProject(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswardValidationProject()

    return render(request, 'first_app/django_form.html', {'form' : form})
