from django import forms 
from . import models 
from django.forms.widgets import NumberInput
import datetime

class ApiForm(forms.Form):
    name = forms.CharField(initial='Your name')
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3}))
    email = forms.EmailField( label="Please enter your email address" )
    agree_our_terms_and_contidion = forms.BooleanField(initial=True)
    date = forms.DateField(initial= datetime.date.today)
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    
    birth_year = forms.DateField(widget= forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect(),choices=FAVORITE_COLORS_CHOICES )
    favorite_colors = forms.MultipleChoiceField(widget= forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES )
    roll_number = forms.IntegerField( help_text = "Enter 6 digit roll number") 
    password = forms.CharField(widget = forms.PasswordInput()) 
    
    GEEKS_CHOICES = ( 
    (1, "A"), 
    (2, "B"), 
    (3, "C"), 
    (4, "D"), 
    (5, "E"), 
    ) 
    typed_choice_field = forms.TypedChoiceField(choices = GEEKS_CHOICES,coerce = str ) 
    duration_field = forms.DurationField( ) 
    file_path_field = forms.FilePathField(path = "practice_project/") 
    url_field = forms.URLField( ) 


class Model_Form(forms.ModelForm):
    class Meta:
        model = models.Model_Form_Model
        fields = "__all__"