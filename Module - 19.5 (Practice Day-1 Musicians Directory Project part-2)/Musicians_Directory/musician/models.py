from django.db import models

# Create your models here.
class Musician(models.Model):

    INSTRUMENT_CHOICES = (
        ('duff', 'Duff'),
        ('flute', 'Flute'),
        ('piano', 'Piano'),
        ('drums', 'Drums'),
        ('guitar', 'Guitar'),
        ('other', 'Other'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    # instrument_type = models.CharField(max_length=200)
    instrument_type = models.CharField(
        max_length=200,
        choices=INSTRUMENT_CHOICES,
        default='other'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"