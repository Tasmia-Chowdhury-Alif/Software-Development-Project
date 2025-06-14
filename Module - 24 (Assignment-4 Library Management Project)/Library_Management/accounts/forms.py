from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .constants import GENDER_TYPE


class UserRegistrationForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    birth_date = forms.DateField(widget= forms.DateInput(attrs={'type' : 'date'}))
    gender = forms.ChoiceField(choices= GENDER_TYPE)
    street_address = forms.CharField(max_length= 100)
    city = forms.CharField(max_length= 100, required= True)
    postal_code = forms.IntegerField(required=True)

    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'profile_picture', 'birth_date', 'gender', 'street_address', 'city', 'postal_code']

    def save(self, commit = True):
        user = super().save(commit= False) # the user instance

        if commit:
            user.save()

            profile_picture = self.cleaned_data.get('profile_picture')
            birth_date = self.cleaned_data.get('birth_date')
            gender = self.cleaned_data.get('gender')
            street_address = self.cleaned_data.get('street_address')
            city = self.cleaned_data.get('city')
            postal_code = self.cleaned_data.get('postal_code')

            Profile.objects.create(
                user= user,
                profile_picture= profile_picture if profile_picture else None,
                birth_date = birth_date,
                gender= gender,
                street_address= street_address,
                city= city,
                postal_code= postal_code, 
            )
        return user 
    

class DepositForm(forms.Form):
    amount = forms.DecimalField(max_digits=12, decimal_places=2)

    # this method is used to validate any form field's input data by naming the it as clean_fieldname
    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        min_deposit_amount = 100

        if amount < min_deposit_amount :
            raise forms.ValidationError(f"Diposit Amount must be at least {min_deposit_amount} $")
        
        return amount