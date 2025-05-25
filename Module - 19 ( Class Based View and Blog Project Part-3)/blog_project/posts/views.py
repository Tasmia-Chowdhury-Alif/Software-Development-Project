from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms, models
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

# Create your views here.

@login_required
def add_post(request):
    if request.method == 'POST': # Checking if the request Method is POST or not 
        post_form = forms.PostForm(request.POST) # providing the user inputed request.POST data to the Model form class_object as Parameter
        if post_form.is_valid(): # Checking that the request.POST data does not contain any error or invalid something
            post_form.instance.author = request.user  # seting the logged in user as the author of the post
            post_form.save() # saving the input data to the database
            return redirect('HomePage') # after successfully saving the data, redirecting to the AddPost page again
    else:
        post_form = forms.PostForm() # in veiws.py model forms needs to be called with ()
    
    return render(request, 'posts/add_post.html', context={'form' : post_form}) # according to best practice django app's templates must contain a folder named as same as the app name. so the template path is posts/add_post.html

# add post using class based view
@method_decorator(login_required, name='dispatch')
class AddPostView(CreateView):
    model = models.Post
    form_class = forms.PostForm 
    template_name = 'posts/add_post.html'
    success_url = reverse_lazy('HomePage')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



@login_required
def edit_post(request, id):
    post = models.Post.objects.get(pk= id) # selecting the specific Post object using get method and primarikey
    post_form = forms.PostForm(instance= post)  
    

    if request.method == 'POST': # Checking if the request Method is POST or not 
        post_form = forms.PostForm(request.POST, instance= post) # providing the specific instance = the post, so that if the user unfortunately click the submit button then a new post with same data does not get created and just update it
        if post_form.is_valid(): # Checking that the request.POST data does not contain any error or invalid something
            post_form.save() # saving the input data to the database
            return redirect('HomePage') # after successfully saving the data, redirecting to the AddPost page again
    
    return render(request, 'posts/add_post.html', context={'form' : post_form}) # according to best practice django app's templates must contain a folder named as same as the app name. so the template path is posts/add_post.html


@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'posts/add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('HomePage')


@login_required
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('HomePage')


@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'Author/delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('HomePage')


class DetailPostView(DetailView):
    model = models.Post
    # pk_url_kwarg = 'pk'
    template_name = 'posts/post_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object() # the Post Model's object is stored here
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object() # the Post Model's object is stored here
        comments = post.comments.all() ### here comments is the reverse relationship for Post model
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context