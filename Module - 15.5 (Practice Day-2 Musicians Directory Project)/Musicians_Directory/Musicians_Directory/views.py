from django.shortcuts import render
from musician.models import Musician 
from album.models import Album 

# Create your views here.
def home(request):
    musicians = Musician.objects.all()
    # albums = Album.objects.all()
    return render(request, 'home.html', context={'musicians' : musicians})