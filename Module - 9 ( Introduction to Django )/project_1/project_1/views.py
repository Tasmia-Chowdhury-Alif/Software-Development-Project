from django.http import HttpResponse

def home(request):
    return HttpResponse("This is home Page")

def contact(request):
    return HttpResponse("This is contact page")