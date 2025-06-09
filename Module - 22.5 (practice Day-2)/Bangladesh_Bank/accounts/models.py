from django.db import models
from django.contrib.auth.models import User
from bank.models import Bank
from .constants import ACCOUNT_TYPE, GENDER_TYPE

# Create your models here.

class UserBankAccount(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'account')
    bank = models.ForeignKey(Bank, on_delete= models.CASCADE, related_name= 'bank')
    account_type = models.CharField(max_length= 10, choices= ACCOUNT_TYPE)
    account_no = models.IntegerField(unique= True)
    birth_date = models.DateField(null= True, blank= True)
    gender = models.CharField(max_length= 10, choices= GENDER_TYPE)
    account_creation_date = models.DateTimeField(auto_now_add = True)
    balance = models.DecimalField(default= 0, max_digits= 12, decimal_places= 2) # this represents the initial balance is 0, the maximum balance limit for an account is 12 Digits with 2 decimal places like 100.55

    def __str__(self):
        return str(self.account_no)

class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'address')
    street_address = models.CharField(max_length= 100)
    city = models.CharField(max_length= 100)
    postal_code = models.PositiveIntegerField()
    country = models.CharField(max_length= 100)
