from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.
def home(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(request, 'home.html', context={'form' : form})