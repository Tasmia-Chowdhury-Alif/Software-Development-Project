from django.shortcuts import render, redirect
from . import forms, models
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
# def add_album(request):
#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('HomePage')
#     else:
#         album_form = forms.AlbumForm()

#     return render(request, 'album/add_album.html', context={'form' : album_form})


@method_decorator(login_required, name='dispatch')
class AddAlbum(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album/add_album.html'
    success_url = reverse_lazy('HomePage')

    def form_valid(self, form):
        messages.success(self.request, 'An Album Created Successfully')
        return super().form_valid(form)
    

# def edit_album(request, id):
#     album_object = models.Album.objects.get(pk= id)
#     album_form = forms.AlbumForm(instance= album_object)

#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST, instance=album_object)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('HomePage')
    
#     return render(request, 'album/add_album.html', context={'form' : album_form})


@method_decorator(login_required, name='dispatch')
class EditAlbum(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    pk_url_kwarg = 'id'
    template_name = 'album/add_album.html'
    success_url = reverse_lazy('HomePage')

    def form_valid(self, form):
        messages.success(self.request, 'Album Edited Successfully')
        return super().form_valid(form)
    