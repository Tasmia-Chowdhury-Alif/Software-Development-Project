from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(default= 0, max_digits= 12, decimal_places= 2) # this represents the initial balance is 0, the maximum balance limit for an account is 12 Digits with 2 decimal places like 100.55
    is_bankrupt = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add=True)