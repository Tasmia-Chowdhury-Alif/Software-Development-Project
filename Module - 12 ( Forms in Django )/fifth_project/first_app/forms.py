from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="User Name : ", help_text="Enter your full name here with in 50 letters", required= True, widget= forms.Textarea(attrs= {'id' : 'text_area1', 'class' : 'class1 class2', 'placeholder' : 'Enter your name'}))
    # file = forms.FileField()
    email = forms.EmailField(label="User Email")
    age = forms.CharField(widget= forms.NumberInput())
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget= forms.DateInput(attrs= {'type' : 'date'}))
    appoinment = forms.DateTimeField(widget= forms.DateInput(attrs= {'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    size = forms.ChoiceField(choices=CHOICES, widget= forms.RadioSelect )
    MEAL = [('P', 'Paperoni'), ('M', 'Mushroom'), ('B', 'Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget= forms.CheckboxSelectMultiple)

# class StudentData(forms.Form):
#     name = forms.CharField(widget= forms.TextInput)
#     email = forms.EmailField(widget= forms.EmailInput)

#     # def clean_name(self) :
#     #     val_name = self.cleaned_data['name']

#     #     if len(val_name) < 10 :
#     #         raise forms.ValidationError("Enter a name with at least 10 cherecters")
#     #     return val_name
    
#     # def clean_email(self) :
#     #     val_email = self.cleaned_data['email']

#     #     if ".com" not in  val_email :
#     #         raise forms.ValidationError("Your email must contain .com")
#     #     return val_email

#     def clean(self):
#         cleaned_data = super().clean()
#         val_name = self.cleaned_data['name']
#         val_email = self.cleaned_data['email']
#         if len(val_name) < 10 :
#             raise forms.ValidationError("Enter a name with at least 10 cherecters")
    
#         if ".com" not in  val_email :
#             raise forms.ValidationError("Your email must contain .com")



class StudentData(forms.Form):
    name = forms.CharField(widget= forms.TextInput, validators=[validators.MinLengthValidator(10)])
    email = forms.EmailField(widget= forms.EmailInput, validators= [validators.EmailValidator])
    age = forms.IntegerField(validators=[validators.MinValueValidator(1, message="age must be at least 1"), validators.MaxValueValidator(150, message="age must be at max 150")])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'jpg'], message= 'the file must be a pdf')])

class PasswardValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    passward = forms.CharField(widget=forms.PasswordInput)
    confirm_passward = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        val_name = self.cleaned_data['name']
        val_pass = self.cleaned_data['passward']
        val_confirmpass = self.cleaned_data['confirm_passward']

        if len(val_name) < 10 :
            raise forms.ValidationError("Enter a name with at least 10 cherecters")
        if val_confirmpass != val_pass :
            raise forms.ValidationError("Passward didn't match")