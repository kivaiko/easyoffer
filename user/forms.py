from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        max_length=150,
        widget=forms.TextInput(attrs={'autofocus': True}),
        label='Email'
    )

    class Meta:
        model = CustomUser
