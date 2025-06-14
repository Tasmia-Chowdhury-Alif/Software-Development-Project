from django.shortcuts import render, redirect
from . import models
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.contrib import messages


# Create your views here.
class BookDetailsView(DetailView):
    model = models.Book
    # pk_url_kwarg = 'pk'
    template_name = 'books/details.html'
    # in DetailView, context data of the selected object is autometically send as singular name of the model like 'book' for this case 


    # def post(self, request, *args, **kwargs):
    #     car = self.get_object()
    #     comment_form = forms.CommentForm(data= self.request.POST)

    #     if comment_form.is_valid():
    #         form_instance = comment_form.save(commit=False)
    #         form_instance.car = car 
    #         form_instance.save()
    #     return self.get(request, *args, **kwargs)

        # name = request.POST.get('name')
        # comment = request.POST.get('comment')

        # if name and comment :
        #     models.Comment.objects.create(
        #         car = car,
        #         name = name,
        #         comment = comment,
        #     )
        # return redirect(request.path)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     car = self.get_object()
    #     comments = car.comments.all()
    #     context["form"] = forms.CommentForm()
    #     context["comments"] = comments
    #     return context