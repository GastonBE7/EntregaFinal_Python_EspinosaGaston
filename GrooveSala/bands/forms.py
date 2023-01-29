from django import forms

from bands.models import Band

class BandForm(forms.ModelForm):
    
    class Meta:
        model = Band
        fields = '__all__'