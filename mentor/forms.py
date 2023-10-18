from django import forms
from django.forms import ModelForm
from django.conf import settings
from ckeditor.widgets import CKEditorWidget
from .models import *


class MentorForm(forms.ModelForm):
    image = forms.FileField(required=False)

    class Meta:
        model = Mentor
        fields = ['name', 'surname', 'username', 'description', 'topics', 'profession', 'skills', 'experience',
                  'about_me', 'cost_30m', 'cost_1h', 'telegram', 'instagram', 'linkedin', 'behance', 'github',
                  'website', 'image', 'public']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'topics': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'profession': forms.SelectMultiple(attrs={'class': 'form-select'}),
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
            'public': 'Опубликовать профиль',
        }


class MentorFilterForm(forms.Form):
    profession = forms.ModelChoiceField(
        queryset=Profession.objects.all().order_by('title'),
        required=True,
        label='Направление:',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    topics = forms.ModelChoiceField(
        queryset=Topic.objects.all(),
        required=False,
        label='Цель:',
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

    RATING_CHOICES = (
        (5, 5),
        (4, 4),
        (3, 3),
        (2, 2),
        (1, 1),
    )

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Оценка:'
    )

    class Meta:
        model = Review
        exclude = ['public', 'created_at', 'mentor']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.CharField(label='Ответ', widget=CKEditorWidget()),
            # 'rating': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'author': 'Ваше имя:',
            # 'rating': 'Оценка:',
        }

