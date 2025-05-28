from django.shortcuts import render
from musician.models import Musician 
from album.models import Album 
from django.views.generic import TemplateView

# Create your views here.
# def home(request):
#     musicians = Musician.objects.all()
#     # albums = Album.objects.all()
#     return render(request, 'home.html', context={'musicians' : musicians})


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        musicians = Musician.objects.all()
        context['musicians'] = musicians
        return context