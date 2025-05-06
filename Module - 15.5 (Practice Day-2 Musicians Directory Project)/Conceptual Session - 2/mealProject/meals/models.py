from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Food(models.Model):
    food_name = models.CharField(max_length=250)
    food_description = models.CharField(max_length=550)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)