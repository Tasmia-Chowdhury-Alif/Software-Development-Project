from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserBankAccount, UserAddress
from bank.models import Bank
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

            default_bank = Bank.objects.get(name= "BD Bank")

            account_type = self.cleaned_data.get('account_type')
            birth_date = self.cleaned_data.get('birth_date')
            gender = self.cleaned_data.get('gender')
            street_address = self.cleaned_data.get('street_address')
            city = self.cleaned_data.get('city')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')

            UserBankAccount.objects.create(
                user = user,
                bank = default_bank, # default bank for Every Account
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



class UserUpdateForm(forms.ModelForm):
    account_type = forms.ChoiceField(choices= ACCOUNT_TYPE)
    birth_date = forms.DateField(widget= forms.DateInput(attrs={'type' : 'date'}))
    gender = forms.ChoiceField(choices= GENDER_TYPE)
    street_address = forms.CharField(max_length= 100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length= 100)

    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'email',]

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
        
        if self.instance :
            try:
                user_account = self.instance.account
                user_address = self.instance.address

            except UserBankAccount.DoesNotExist:
                user_account = None
                user_address = None

            if (user_account and user_address) : #########
                self.fields['account_type'].initial = user_account.account_type
                self.fields['birth_date'].initial = user_account.birth_date
                self.fields['gender'].initial = user_account.gender
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['postal_code'].initial = user_address.postal_code
                self.fields['country'].initial = user_address.country



    def save(self, commit = True):
        user = super().save(commit= False) # creating the user instance without saving it 

        if commit :
            user.save()

            user_account = user.account # it's working as same as UserBankAccount.objects.get(user= user)
            user_address = user.address # it's working as same as UserAddress.objects.get(user= user)

            user_account.account_type = self.cleaned_data.get('account_type')
            user_account.birth_date = self.cleaned_data.get('birth_date')
            user_account.gender = self.cleaned_data.get('gender')
            user_account.save()

            user_address.street_address = self.cleaned_data.get('street_address')
            user_address.city = self.cleaned_data.get('city')
            user_address.postal_code = self.cleaned_data.get('postal_code')
            user_address.country = self.cleaned_data.get('country')
            user_account.save()


        return user 
    
