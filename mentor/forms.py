from django import forms
from django.forms import ModelForm
from django.conf import settings
from .models import *


class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        exclude = ['public', 'created_at', 'priority']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя:'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'utc': forms.Select(attrs={'class': 'form-select'}),
            'skills': forms.CheckboxSelectMultiple(),
            'topics': forms.CheckboxSelectMultiple(),
            'directions': forms.CheckboxSelectMultiple(),
            'pay_methods': forms.CheckboxSelectMultiple(),
            'tags': forms.CheckboxSelectMultiple(),
            'country_Experience_online': forms.SelectMultiple(),
            'country_Experience_offline': forms.CheckboxSelectMultiple(),
            'languages': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_30m': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_1h': forms.NumberInput(attrs={'class': 'form-control'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.NumberInput(attrs={'class': 'form-control'}),
            'cv_link': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'portfolio': forms.URLInput(attrs={'class': 'form-control'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Имя:',
            'surname': 'Фамилия:',
            'username': 'Username:',
            'profession': 'Должность:',
            'utc': 'Часовой пояс:',
            'skills': 'Навыки:',
            'topics': 'Могу помочь:',
            'directions': 'Направление:',
            'pay_methods': 'Принимаю оплату:',
            'tags': 'Теги:',
            'country_Experience_online': 'Online опыт работы на страны:',
            'country_Experience_offline': 'Offline опыт работы на страны::',
            'languages': 'Языки:',
            'experience': 'Опыт в годах:',
            'cost_30m': 'Цена консультации 30 мин.:',
            'cost_1h': 'Цена консультации 1 час.:',
            'telegram': 'Telegram username:',
            'whatsapp': 'Whatsapp телефон:',
            'cv_link': 'Ссылка на CV:',
            'linkedin': 'LinkedIn ссылка:',
            'github': 'Github ссылка:',
            'portfolio': 'Ссылка на портфолио:',
            'about_me': 'О себе:',
        }


