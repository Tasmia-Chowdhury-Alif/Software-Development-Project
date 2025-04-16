from django import forms
from django.core import validators 

class contactForm(forms.Form):
    name = forms.CharField(label="User Name", help_text="full name", widget= forms.TextInput(attrs= {'id' : 'name_text_area', 'class' : 'class1 class2 text-primary', 'placeholder' : 'Enter Your Full Name'}))
    email = forms.EmailField()
    # file = forms.FileField()
    age = forms.IntegerField(widget=forms.NumberInput())
    weight = forms.FloatField(widget=forms.NumberInput())
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    birthday = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    appoinment = forms.DateTimeField(widget= forms.DateTimeInput(attrs={'type' : 'datetime-local'}))
    SIZE = [('S',"Small"),('M',"Medium"),('L','Large'),('XL','Extra Large')]
    size = forms.ChoiceField(choices= SIZE, widget= forms.RadioSelect())
    ITEM = [('B','Beef'),('C','Chicken'),('M','Mango')]
    pizza = forms.MultipleChoiceField(choices= ITEM, widget= forms.CheckboxSelectMultiple())
    

# class studentForm(forms.Form):
#     name = forms.CharField(widget= forms.TextInput())
#     email = forms.EmailField(widget= forms.EmailInput())

#     def clean(self):
#         # cleande_data = super().clean() is necessery when this class inherits a custom class 
#         cleaned_data = super().clean()
#         var_name = self.cleaned_data['name']
#         var_email = self.cleaned_data['email']

#         if len(var_name) < 3 or len(var_name) > 10:
#             raise forms.ValidationError("Name must be greater than 3 and less then 10")
#         if '.com' not in var_email :
#             raise forms.ValidationError("Email must contain .com")

def custom_validator(value):
    if value < 20 :
        raise forms.ValidationError("Age must be greater than 20")

class studentForm(forms.Form):
    name = forms.CharField(widget= forms.TextInput(), validators=[validators.MinLengthValidator(2, message="Name must have at least 2 charecters")])
    email = forms.EmailField(widget= forms.EmailInput(), validators=[validators.EmailValidator(message="Enter a valid Email")])
    age = forms.IntegerField(widget= forms.NumberInput(), validators=[custom_validator])
    file = forms.FileField(widget= forms.FileInput(), validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg'], message=".pdf and .jpg files only")])

class passwardValidation(forms.Form):
    name = forms.CharField(widget= forms.TextInput)
    email = forms.EmailField(widget= forms.EmailInput)
    passward = forms.CharField(widget= forms.PasswordInput)
    confirm_passward = forms.CharField(widget= forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        valpass = self.cleaned_data['passward']
        valrepass = self.cleaned_data['confirm_passward']

        if len(valname) < 2 :
            raise forms.ValidationError("Name Lenght Must be Greater than 2")
        
        if valpass != valrepass :
            raise forms.ValidationError("Passward doesn't match")
