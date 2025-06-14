from django.db import models
from category.models import Category

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    category = models.ManyToManyField(Category, related_name= 'books')
    image = models.ImageField(upload_to='books/images/', null=True, blank=True) # to save the uploaded image specifically to the app's inner media directory you need to comment out the MEDIA_ROOT = BASE_DIR / 'media' at settings.py

    def __str__(self):
        return f'{self.id} {self.title}' 