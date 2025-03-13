from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("This is second_app About page")