from django.shortcuts import render, redirect
from . import forms, models 

# Create your views here.
def add_musician(request):

    if request.method == 'POST' :
        musician_form = forms.MusicianForm(request.POST)

        if musician_form.is_valid():
            musician_form.save()
            return redirect('HomePage')
    else:
        musician_form = forms.MusicianForm()

    return render(request, 'musician/add_musician.html', context={ 'form' : musician_form})

def edit_musician(request, id):
    musician_object = models.Musician.objects.get(pk= id)
    musician_form = forms.MusicianForm(instance= musician_object)

    if request.method == "POST":
        musician_form = forms.MusicianForm(request.POST, instance= musician_object)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('HomePage')
    
    return render(request, 'musician/add_musician.html', context={ 'form' : musician_form})

def delete_musician(request, id):
    musician_object = models.Musician.objects.get(pk= id)
    musician_object.delete()
    return redirect('HomePage')