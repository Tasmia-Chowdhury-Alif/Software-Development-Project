from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # Many to Many relationship because = one post can have multiple category and also one category can contain multiple posts
    author = models.ForeignKey(Author, on_delete=models.CASCADE) # Many to one relationship because = Multiple posts can have same author and also one author can have multiple posts
    
    def __str__(self):
        return self.title