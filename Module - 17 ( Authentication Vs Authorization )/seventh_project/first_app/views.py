from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def home(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            messages.success(request, 'Account Created Successfully')
            # messages.warning(request, 'Warning message')
            # messages.info(request, 'Info message')
            return redirect('homepage')

    return render(request, 'home.html', context={'form' : form})