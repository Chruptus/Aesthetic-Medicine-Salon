from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Client

class UserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class ClientForm(forms.ModelForm): 
    class Meta:
        model = Client
        fields = ['phone_number']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ClientUpdateForm(forms.ModelForm): 
    class Meta:
        model = Client
        fields = ['phone_number']