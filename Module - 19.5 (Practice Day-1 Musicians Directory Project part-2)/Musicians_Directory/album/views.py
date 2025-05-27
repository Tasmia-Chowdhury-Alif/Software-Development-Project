from django.shortcuts import render, redirect
from . import forms, models

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('HomePage')
    else:
        album_form = forms.AlbumForm()

    return render(request, 'album/add_album.html', context={'form' : album_form})

def edit_album(request, id):
    album_object = models.Album.objects.get(pk= id)
    album_form = forms.AlbumForm(instance= album_object)

    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album_object)
        if album_form.is_valid():
            album_form.save()
            return redirect('HomePage')
    
    return render(request, 'album/add_album.html', context={'form' : album_form})