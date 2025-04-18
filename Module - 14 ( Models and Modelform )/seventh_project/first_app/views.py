from django.shortcuts import render
from .form import StudentForm

# Create your views here.
def home(request):
    if request.method == 'POST' :
        form = StudentForm(request.POST)
        if form.is_valid() :
            form.save()
            print(form.cleaned_data)
    else :
        form = StudentForm
    return render(request, 'first_app/home.html', context={'form' : form})