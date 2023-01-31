from django import forms

from bands.models import Band, Turn

class BandForm(forms.ModelForm):
    
    class Meta:
        model = Band
        fields = '__all__'


class TurnForm(forms.ModelForm):

    class Meta:
        model = Turn
        fields = ['turn_assigned', 'own_instruments']