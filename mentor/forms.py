from django import forms
from django.forms import ModelForm
from django.conf import settings
from ckeditor.widgets import CKEditorWidget
from .models import *


class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        exclude = ['created_at', 'priority', 'last_update', 'permission']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'topics': forms.CheckboxSelectMultiple(),
            'profession': forms.CheckboxSelectMultiple(),
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
            'public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'name': 'Имя:',
            'surname': 'Фамилия:',
            'username': 'Username:',
            'description': 'Должность:',
            'topics': 'Могу помочь:',
            'profession': 'Направление:',
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
            'public': 'В публичном доступе',
        }


# class MentorFilterForm(forms.ModelForm):
#     class Meta:
#         model = Mentor
#         exclude = ['public', 'created_at', 'priority', 'name', 'surname', 'username', 'profession', 'experience',
#                    'cost_30m', 'cost_1h', 'telegram', 'instagram', 'linkedin', 'github', 'behance', 'website',
#                    'about_me', 'image', 'skills', 'last_update', 'user', 'permission', 'description', 'topics']
#         widgets = {
#             'profession': forms.Select(attrs={'class': 'form-select'}),
#         }
#         labels = {
#             'profession': 'Направление:',
#         }


class MentorFilterForm(forms.Form):
    profession = forms.ModelChoiceField(
        queryset=Profession.objects.all(),
        required=False,
        label='По профессии',
        widget=forms.Select(attrs={'class': 'form-select'})
    )


class DirectionFilterForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['profession']
        widgets = {
            'profession': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'profession': 'Направление:',
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ['public', 'created_at', 'mentor']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.CharField(label='Ответ', widget=CKEditorWidget()),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'author': 'Ваше имя:',
            'rating': 'Оценка:',
        }

