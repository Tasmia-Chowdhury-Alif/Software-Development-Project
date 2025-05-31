from django.shortcuts import render
from . import models
from django.views.generic import DetailView

# Create your views here.
class CarDetailsView(DetailView):
    model = models.Car
    # pk_url_kwarg = 'pk'
    template_name = 'cars/details.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["car"] = 
    #     return context
    
