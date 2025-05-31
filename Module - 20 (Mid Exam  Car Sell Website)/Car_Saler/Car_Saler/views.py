from django.shortcuts import render
from django.views.generic import ListView
from cars.models import Car, Brand
from django.http import Http404

class HomeView(ListView):
    model = Car 
    template_name = 'home.html'
    context_object_name = 'products'

    def get_queryset(self):
        brand_slug = self.kwargs.get('brand_slug')
        
        if brand_slug:
            try:
                brand = Brand.objects.get(slug=brand_slug)

            except Brand.DoesNotExist: # handleing where the brand doesn't exixts but someone requested get request  
                raise Http404("Brand not found")
            
            return Car.objects.filter(brand = brand)
        
        return Car.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        return context
    