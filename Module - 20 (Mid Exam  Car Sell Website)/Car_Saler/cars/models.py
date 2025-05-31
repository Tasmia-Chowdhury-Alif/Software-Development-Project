from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length= 200)
    slug = models.SlugField(max_length= 200, unique= True)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveBigIntegerField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete= models.CASCADE, related_name= 'cars')

    def __str__(self):
        return f'{self.id} {self.name}' 
    
class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete= models.CASCADE, related_name= 'images')
    image = models.ImageField(upload_to= f'car/images/')

    def __str__(self):
        return f"Image{self.id} for {self.car.name}"
    

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'orders')
    car = models.ForeignKey(Car, on_delete= models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)