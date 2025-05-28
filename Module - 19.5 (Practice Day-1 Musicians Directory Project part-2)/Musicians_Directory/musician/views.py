from django.shortcuts import render, redirect 
from . import forms, models 
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
# def add_musician(request):

#     if request.method == 'POST' :
#         musician_form = forms.MusicianForm(request.POST)

#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('HomePage')
#     else:
#         musician_form = forms.MusicianForm()

#     return render(request, 'musician/add_musician.html', context={ 'form' : musician_form})


@method_decorator(login_required, name='dispatch')
class AddMusician(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'musician/add_musician.html'
    success_url = reverse_lazy('HomePage')

    def form_valid(self, form):
        messages.success(self.request, 'The Musician has been Added successfully!')
        return super().form_valid(form)
    


# def edit_musician(request, id):
#     musician_object = models.Musician.objects.get(pk= id)
#     musician_form = forms.MusicianForm(instance= musician_object)

#     if request.method == "POST":
#         musician_form = forms.MusicianForm(request.POST, instance= musician_object)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('HomePage')
    
#     return render(request, 'musician/add_musician.html', context={ 'form' : musician_form})


@method_decorator(login_required, name='dispatch')
class EditMusician(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    pk_url_kwarg = 'id'
    template_name = 'musician/add_musician.html'
    success_url = reverse_lazy('HomePage')

    def form_valid(self, form):
        messages.success(self.request, 'Updated successfully!')
        return super().form_valid(form)


# def delete_musician(request, id):
#     musician_object = models.Musician.objects.get(pk= id)
#     musician_object.delete()
#     return redirect('HomePage')

@method_decorator(login_required, name='dispatch')
class DeleteMusician(DeleteView):
    model = models.Musician
    pk_url_kwarg = 'id'
    template_name = 'user_app/delete.html'
    success_url = reverse_lazy('HomePage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'This Musician'
        return context
    