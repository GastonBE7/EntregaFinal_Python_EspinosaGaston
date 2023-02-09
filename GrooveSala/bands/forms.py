from django import forms

from bands.models import Band, Turn, Event


# <----------------------------------------------- BANDS --------------------------------------------->
class BandForm(forms.ModelForm):
    
    class Meta:
        model = Band
        fields = ['logo', 'name_band', 'members', 'musical_genre', 'ig', 'contact']

class BandUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Turn
        fields = ['logo', 'members', 'musical_genre', 'own_instruments', 'contact']


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'




# <----------------------------------------------- TURNS --------------------------------------------->
class TurnForm(forms.ModelForm):

    class Meta:
        model = Turn
        fields = ['name_band', 'turn_assigned', 'members', 'own_instruments']

class FirstTurnForm(forms.ModelForm):

    class Meta:
        model = Turn
        fields = ['name_band', 'members', 'turn_assigned', 'own_instruments','contact']