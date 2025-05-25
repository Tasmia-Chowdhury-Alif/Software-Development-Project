from django.db import models
from categories.models import Category
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # Many to Many relationship because = one post can have multiple category and also one category can contain multiple posts
    author = models.ForeignKey(User, on_delete=models.CASCADE) # Many to one relationship because = Multiple posts can have same author and also one author can have multiple posts
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='posts/media/uploads/', null=True, blank=True) # to save the uploaded image specifically to the app's inner media directory you need to comment out the MEDIA_ROOT = BASE_DIR / 'media' at settings.py
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Commented by {self.name}'
    