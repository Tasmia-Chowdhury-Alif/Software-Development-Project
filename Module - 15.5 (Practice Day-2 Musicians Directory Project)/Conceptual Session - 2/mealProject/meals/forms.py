from django import forms 
from . import models

class MealAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['food_name'].widget.attrs.update({'class' : 'form-control'})
        for field in self.fields :
            self.fields[field].widget.attrs.update({'class' : 'form-control'})


    class Meta :
        model = models.Food
        fields = '__all__'

        labels = {
            'category' : 'Food Category',
        }

        widgets = {
            'food_description' : forms.Textarea(attrs={'rows': 4})
        }