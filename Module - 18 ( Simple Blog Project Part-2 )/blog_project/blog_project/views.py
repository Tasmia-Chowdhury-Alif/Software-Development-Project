from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home(request, category_slug = None):
    data = Post.objects.all()
    categories = Category.objects.all()
    if category_slug != None :
        category = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = category)
    # print(data)
    return render(request, 'home.html', context={'data' : data, 'category' : categories})