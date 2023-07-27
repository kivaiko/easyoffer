from django import forms
from .models import *


class CommentForm(forms.Form):
    text = forms.CharField(label='Ответ', widget=forms.Textarea)
    author = forms.CharField(max_length=50, label='Автор')


class AddQuestion(forms.Form):
    title = forms.CharField(max_length=255, label='Вопрос:')
    tag = forms.ModelChoiceField(queryset=Tag.objects.all(), empty_label=None, label='Тег:')


class VideoAnswerForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название видео: ')
    url = forms.URLField(label='Ссылка на момент ответа: ')


class ExtraContentForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название: ')
    url = forms.URLField(label='Ссылка: ')
