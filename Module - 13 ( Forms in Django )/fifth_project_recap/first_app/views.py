from django.shortcuts import render
from . forms import contactForm, studentForm, passwardValidation

# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('UserName')
        email = request.POST.get('UserEmail')
    else :
        name = "Name is not submited yet"
        email = "Email is not submited yet"
    return render(request, 'first_app/about.html', context={'name' : name, 'email' : email})
        # return render(request, 'first_app/about.html')

def submit_form(request):
    return render(request, 'first_app/form.html')

def django_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else :
        form = contactForm()
    # if request.method == 'POST' :
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     print(name)
    #     print(email)

    return render(request, 'first_app/django_form.html', context={'form' : form})

def student_form(request):
    if request.method == 'POST':
        form = studentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else :
        form = studentForm()

    return render(request, 'first_app/django_form.html', context={'form' : form})

def passward_form(request):
    if request.method == 'POST':
        form = passwardValidation(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else :
        form = passwardValidation()

    return render(request, 'first_app/django_form.html', context={'form' : form})
