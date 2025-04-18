from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel 
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll',
            'father_name' : "Father's name",
        }
        widgets = {
            'name' : forms.TextInput(attrs= {'class' : 'text-success'}),
            'roll' : forms.NumberInput(),
        }
        help_texts = {
            'name' : 'Write Your full name',
        }
        error_messages = {
            'name' : { 'required' : 'Your name is required'},
        }
