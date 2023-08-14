from django import forms
from .models import *


class CommentForm(forms.Form):
    text = forms.CharField(label='Ответ', widget=forms.Textarea)
    author = forms.CharField(max_length=50, label='Автор')


class AddQuestion(forms.Form):
    title = forms.CharField(max_length=255, label='Вопрос:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    tag = forms.ModelChoiceField(queryset=Tag.objects.all(), empty_label=None, label='Тег:',
                                 widget=forms.Select(attrs={'class': 'form-select'}))


class VideoAnswerForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название видео: ',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.URLField(label='Ссылка на момент ответа: ', widget=forms.URLInput(attrs={'class': 'form-control'}))


class ExtraContentForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название: ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.URLField(label='Ссылка: ', widget=forms.URLInput(attrs={'class': 'form-control'}))


class MockForm(forms.ModelForm):
    class Meta:
        model = MockInterview
        exclude = ['public', 'url', 'title', 'created_at']
        widgets = {
            'profession': forms.Select(attrs={'class': 'form-select'}),
            'grade': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'profession': 'Должность:',
            'grade': 'Грейд:',
        }

