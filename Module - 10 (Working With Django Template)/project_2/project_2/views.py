from django.shortcuts import render 

def idx(request):
    return render(request, 'index.html')