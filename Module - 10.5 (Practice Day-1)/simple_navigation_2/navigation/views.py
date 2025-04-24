from django.shortcuts import render

# Create your views here.
def nav(request):
    return render(request, 'navigation/nav.html')

def more(request):
    return render(request, 'navigation/more.html')

def services(request):
    return render(request, 'navigation/services.html')
