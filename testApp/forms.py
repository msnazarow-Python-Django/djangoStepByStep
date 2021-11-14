from django import forms
from .models import *

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}
    ))
    password = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password' }))
    email = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Phone'}))


class RegistrationModal(forms.ModelForm):
    class Meta:
        model = RegistrationData

        fields = [
            'username',
            'password',
            'email',
            'phone'
        ]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'password':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'email':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'phone':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone'})
        }