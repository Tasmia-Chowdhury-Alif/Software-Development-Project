from django.shortcuts import render, redirect
from . import forms 

# Create your views here.
def add_post(request):
    if request.method == 'POST': # Checking if the request Method is POST or not 
        post_form = forms.PostForm(request.POST) # providing the user inputed request.POST data to the Model form class_object as Parameter
        if post_form.is_valid(): # Checking that the request.POST data does not contain any error or invalid something
            post_form.save() # saving the input data to the database
            return redirect('AddPost') # after successfully saving the data, redirecting to the AddPost page again
    else:
        post_form = forms.PostForm() # in veiws.py model forms needs to be called with ()
    
    return render(request, 'posts/add_post.html', context={'form' : post_form}) # according to best practice django app's templates must contain a folder named as same as the app name. so the template path is posts/add_post.html