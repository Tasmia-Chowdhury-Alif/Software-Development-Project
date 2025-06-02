from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserBankAccount, UserAddress
from .constants import ACCOUNT_TYPE, GENDER_TYPE


class UserRegistrationForm(UserCreationForm):
    account_type = forms.ChoiceField(choices= ACCOUNT_TYPE)
    birth_date = forms.DateField(widget= forms.DateInput(attrs={'type' : 'date'}))
    gender = forms.ChoiceField(choices= GENDER_TYPE)
    street_address = forms.CharField(max_length= 100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length= 100)

    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'account_type', 'birth_date', 'gender', 'street_address', 'city', 'postal_code', 'country']

    def save(self, commit = True):
        user = super().save(commit= False) # creating the user instance without saving it 

        if commit :
            user.save()
            account_type = self.cleaned_data.get('account_type')
            birth_date = self.cleaned_data.get('birth_date')
            gender = self.cleaned_data.get('gender')
            street_address = self.cleaned_data.get('street_address')
            city = self.cleaned_data.get('city')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')

            UserBankAccount.objects.create(
                user = user,
                account_type = account_type,
                account_no = 100000 + user.id,
                birth_date = birth_date,
                gender = gender
            )

            UserAddress.objects.create(
                user = user,
                street_address = street_address,
                city = city,
                postal_code = postal_code,
                country = country
            )

        return user 
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class' : (
                            'appearance-none block w-full bg-gray-200 '
                            'text-gray-700 border border-gray-200 rounded '
                            'py-3 px-4 leading-tight focus:outline-none '
                            'focus:bg-white focus:border-gray-500'
                ) 
            })