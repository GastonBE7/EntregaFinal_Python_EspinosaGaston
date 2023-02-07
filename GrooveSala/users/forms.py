from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from users.models import UserProfile

class RegisterForm(UserCreationForm):
    name_band = forms.CharField(max_length=100, required=True, label='Nombre grupo/banda')
    ig = forms.CharField(max_length=100, required=True, label='@(instagram)')

    class Meta:
        model = User
        fields = ['username', 'email', 'name_band', 'ig', 'password1','password2']

class UserUpdateForm(forms.ModelForm):
    name_band = forms.CharField(max_length=100, required=True, label='Nombre grupo/banda')
    ig = forms.CharField(max_length=100, required=True, label='@(instagram)')
    class Meta:
        model = User
        fields = ['name_band', 'ig']

class UserProfileForm(forms.ModelForm):
    members=forms.IntegerField(label='Nro de Integrantes')
    musical_genre=forms.CharField(max_length=100, label='Genero/estilo')

    class Meta:
        model = UserProfile
        fields = ['members', 'musical_genre', 'contact', 'profile_picture']