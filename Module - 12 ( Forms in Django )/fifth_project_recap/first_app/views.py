from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'first_app/home.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('UserName')
        email = request.POST.get('UserEmail')
    else :
        name = "Name is not submited yet"
        email = "Email is not submited yet"
    return render(request, 'first_app/about.html', context={'name' : name, 'email' : email})
        # return render(request, 'first_app/about.html')

def submint_form(request):
    return render(request, 'first_app/form.html')
