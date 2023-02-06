from django import forms

class BeverageForm(forms.Form):

    brand =forms.CharField(max_length=100)
    size =forms.IntegerField(label='En ml. (Ej: 473ml)')
    quantity = forms.IntegerField()