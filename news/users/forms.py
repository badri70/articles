from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class AuthenticatedUser(AuthenticationForm):
    username = forms.CharField(max_length=75, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


