from django import forms

from beverages.models import Beverage

class BeverageForm(forms.ModelForm):
    class Meta:
        model = Beverage
        fields = ['picture', 'brand', 'size', 'quantity']

    