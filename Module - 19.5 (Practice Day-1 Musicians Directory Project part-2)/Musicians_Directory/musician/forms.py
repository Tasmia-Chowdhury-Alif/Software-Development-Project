from django import forms
from . import models

class MusicianForm(forms.ModelForm):
    # This widget will not be shown in the admin interface. 
    # INSTRUMENT_CHOICES = (
    #     ('guitar', 'Guitar'),
    #     ('piano', 'Piano'),
    #     ('drums', 'Drums'),
    #     ('flute', 'Flute'),  # Different choices from model
    # )
    # instrument_type = forms.ChoiceField(choices=INSTRUMENT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = models.Musician
        fields = '__all__'
        widgets = {
            # 'instrument_type': forms.RadioSelect(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={
                # 'class': 'form-control',
                'type': 'tel',  # Optimizes for phone input on mobile
                'placeholder': '+880 01XXXXXXXXX',
            }),
        }

