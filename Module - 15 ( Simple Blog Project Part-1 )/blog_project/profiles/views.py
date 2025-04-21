from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profile_form = forms.ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('AddProfile')
    else:
        profile_form = forms.ProfileForm()
    
    return render(request, 'profiles/add_profile.html', context={'form' : profile_form})
    