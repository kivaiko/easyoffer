from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['create_at']


class CustomUserAuthenticationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['create_at']
