from django.shortcuts import render, redirect
from musician import forms

# Create your views here.
def add_musician(request):
    context= {}
    if request.method == 'POST' :
        context['form'] = forms.MusicianForm(request.POST)

        if context['form'].is_valid():
            context['form'].save()
            return redirect('HomePage')
    else:
        context['form'] = forms.MusicianForm()

    return render(request, 'musician/add_musician.html', context)