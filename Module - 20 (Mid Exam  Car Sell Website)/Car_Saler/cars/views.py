from django.shortcuts import render, redirect
from . import models, forms 
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib import messages

# Create your views here.
class CarDetailsView(DetailView):
    model = models.Car
    # pk_url_kwarg = 'pk'
    template_name = 'cars/details.html'
    # in DetailView, context data of the selected object is autometically send as singular name of the model like 'car' for this case 


    def post(self, request, *args, **kwargs):
        car = self.get_object()
        comment_form = forms.CommentForm(data= self.request.POST)

        if comment_form.is_valid():
            form_instance = comment_form.save(commit=False)
            form_instance.car = car 
            form_instance.save()
        return self.get(request, *args, **kwargs)

        # name = request.POST.get('name')
        # comment = request.POST.get('comment')

        # if name and comment :
        #     models.Comment.objects.create(
        #         car = car,
        #         name = name,
        #         comment = comment,
        #     )
        # return redirect(request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        comments = car.comments.all()
        context["form"] = forms.CommentForm()
        context["comments"] = comments
        return context
    

class BuyNowView(LoginRequiredMixin, View):
    def post(self, request, pk):
        car = models.Car.objects.get(pk= pk)

        if car.quantity > 0:
            with transaction.atomic():
                models.Order.objects.create(owner = self.request.user, car = car)

                car.quantity -= 1
                car.save()
                messages.success(self.request, f"You have successfully bought The {car.name}")
        else : 
            messages.warning(self.request, f"This car is out of stock")
        
        return redirect('DetailsPage', pk= car.pk)