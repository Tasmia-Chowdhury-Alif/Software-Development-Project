from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    RATTING_CHOICES = (
        ('1','⭐'),
        ('2','⭐⭐'),
        ('3','⭐⭐⭐'),
        ('4','⭐⭐⭐⭐'),
        ('5','⭐⭐⭐⭐⭐'),
    )

    album_name = models.CharField(max_length=200)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    album_release_date = models.DateField(auto_now_add=True)
    rating = models.CharField(max_length=20, choices=RATTING_CHOICES, default='1')

    def __str__(self):
        return self.album_name