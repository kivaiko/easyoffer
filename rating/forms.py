from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['question', 'rating', 'public', 'created_at']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.CharField(widget=CKEditorWidget()),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'author': 'Автор/Источник:',
            'url': 'Ссылка(не обяз.):',
        }


class AddQuestion(forms.Form):
    title = forms.CharField(max_length=255, label='Вопрос:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    tag = forms.ModelChoiceField(queryset=Tag.objects.all(), empty_label=None, label='Тег:',
                                 widget=forms.Select(attrs={'class': 'form-select'}))


class QuestionSearchForm(forms.Form):
    search_query = forms.CharField(label='Поиск', required=False, widget=forms.TextInput(attrs={'class': 'form-control me-2', 'placeholder': "Поиск вопроса", 'aria-label': "Search"}))


class VideoAnswerForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название видео: ',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.URLField(label='Ссылка на момент ответа: ', widget=forms.URLInput(attrs={'class': 'form-control'}))


class ExtraContentForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название: ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.URLField(label='Ссылка: ', widget=forms.URLInput(attrs={'class': 'form-control'}))


class MockFilterForm(forms.ModelForm):
    # profession = forms.ModelChoiceField(queryset=Profession.objects.all().order_by('title'))

    class Meta:
        model = MockInterview
        exclude = ['public', 'url', 'title', 'created_at']
        widgets = {
            'profession': forms.Select(attrs={'class': 'form-select'}),
            'grade': forms.RadioSelect(),
        }
        labels = {
            'profession': 'Должность:',
            'grade': 'Грейд:',
        }

    def __init__(self, *args, **kwargs):
        super(MockFilterForm, self).__init__(*args, **kwargs)
        self.fields['profession'].queryset = Profession.objects.all().order_by('title')


class AddMockForm(forms.ModelForm):
    class Meta:
        model = MockInterview
        exclude = ['public', 'created_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'profession': forms.Select(attrs={'class': 'form-select'}),
            'grade': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'profession': 'Должность:',
            'title': 'Название:',
            'url': 'Ссылка:',
            'grade': 'Грейд:',
        }
