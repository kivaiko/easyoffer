from django import forms
from django.forms import ModelForm
from django.conf import settings
from .models import *


class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        exclude = ['public', 'created_at', 'priority']
        # 'additional_service_1_title', 'additional_service_1_description', 'additional_service_1_price', 'additional_service_2_title', 'additional_service_2_description', 'additional_service_2_price', 'page_views', 'page_display', 'telegram_link_clicks', 'instagram_link_clicks', 'linkedin_link_clicks', 'github_link_clicks', 'behance_link_clicks', 'website_link_clicks', 'last_update'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'topics': forms.CheckboxSelectMultiple(),
            'directions': forms.CheckboxSelectMultiple(),
            'skills': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control'}),
            'cost_30m': forms.NumberInput(attrs={'class': 'form-control'}),
            'cost_1h': forms.NumberInput(attrs={'class': 'form-control'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
            'behance': forms.URLInput(attrs={'class': 'form-control'}),
            'github': forms.URLInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Имя:',
            'surname': 'Фамилия:',
            'username': 'Username:',
            'profession': 'Должность:',
            'topics': 'Могу помочь:',
            'directions': 'Направление:',
            'skills': 'Навыки:',
            'experience': 'Опыт:',
            'cost_30m': '30 мин:',
            'cost_1h': '1 час:',
            'telegram': 'Telegram:',
            'instagram': 'Instagram:',
            'linkedin': 'LinkedIn:',
            'github': 'Github:',
            'behance': 'Behance:',
            'website': 'Сайт:',
            'about_me': 'О себе:',
            'image': 'Фото:',
        }


class MentorFilterForm(forms.ModelForm):
    class Meta:
        model = Mentor
        exclude = ['public', 'created_at', 'priority', 'name', 'surname', 'username', 'profession', 'experience',
                   'cost_30m', 'cost_1h', 'telegram', 'instagram', 'linkedin', 'github', 'behance', 'website',
                   'about_me', 'image', 'skills']
        # 'additional_service_1_description', 'additional_service_1_price', 'additional_service_2_title', 'additional_service_2_description', 'additional_service_2_price', 'page_views', 'page_display', 'telegram_link_clicks', 'instagram_link_clicks', 'linkedin_link_clicks', 'github_link_clicks', 'behance_link_clicks', 'website_link_clicks', 'last_update'
        widgets = {
            'directions': forms.Select(attrs={'class': 'form-select'}),
            'topics': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'directions': 'Направление:',
            'topics': 'Тип вопроса:',
        }

