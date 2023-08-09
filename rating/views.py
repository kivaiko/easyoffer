from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.db.models import F, Value
from .forms import *
from .models import *


class IndexView(ListView):
    """Список профессий"""
    template_name = 'index.html'
    model = Profession
    queryset = Profession.objects.filter(public_rating=True)


def profession(request, prof_slug):
    if request.method == "POST":
        form = AddQuestion(request.POST)
        if form.is_valid():
            Question.objects.create(
                title=form.cleaned_data["title"],
                tag=form.cleaned_data["tag"]
            )
            Rating.objects.create(
                profession=Profession.objects.get(prof_slug=prof_slug),
                question=Question.objects.latest('id')
            )
            return redirect('thx_data')

    form = AddQuestion()
    prof_data = Profession.objects.get(prof_slug=prof_slug)
    ratings = Rating.objects.select_related('question').filter(profession=prof_data, public=True).order_by("-rating").annotate(chance=F('rating') * 100 / prof_data.votes)
    return render(request, 'question_rating.html', {
        'prof_data': prof_data,
        'ratings': ratings,
        'form': form
    })


def question(request, question_id):
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        video_form = VideoAnswerForm(request.POST, prefix='video')
        extra_content_form = ExtraContentForm(request.POST, prefix='content')
        if comment_form.is_valid():
            Answer.objects.create(
                question_id=question_id,
                text=comment_form.cleaned_data["text"],
                author=comment_form.cleaned_data["author"]
            )
            return redirect('thx_data')
        if video_form.is_valid():
            VideoAnswerLink.objects.create(
                question_id=question_id,
                title=video_form.cleaned_data["title"],
                url=video_form.cleaned_data["url"]
            )
            return redirect('thx_data')
        if extra_content_form.is_valid():
            ExtraContentLink.objects.create(
                question_id=question_id,
                title=extra_content_form.cleaned_data["title"],
                url=extra_content_form.cleaned_data["url"]
            )
            return redirect('thx_data')
    comment_form = CommentForm()
    video_answer_form = VideoAnswerForm(prefix='video')
    extra_content_form = ExtraContentForm(prefix='content')
    question_data = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question__id=question_data.id, public=True)
    video_links = VideoAnswerLink.objects.filter(question__id=question_data.id, public=True)
    extra_links = ExtraContentLink.objects.filter(question__id=question_data.id, public=True)
    return render(request, 'question.html', {
        'comment_form': comment_form,
        'video_answer_form': video_answer_form,
        'extra_content_form': extra_content_form,
        'question_data': question_data,
        'answers': answers,
        'video_links': video_links,
        'extra_links': extra_links,
    })


def quiz(request, prof_slug):
    if request.method == "POST":
        for i in request.POST:
            if request.POST[i] == "Встречался":
                question = Rating.objects.get(id=i)
                question.rating += 1
                question.save()
        # q = Rating.objects.filter(id__in=ids)
        return redirect('profession', prof_slug=prof_slug)
    prof_data = Profession.objects.get(prof_slug=prof_slug)
    ratings = Rating.objects.select_related('question').filter(profession=prof_data, public=True).order_by("-rating")
    return render(request, 'quiz.html', {
        'prof_data': prof_data,
        'ratings': ratings,
    })


class ThxView(TemplateView):
    """Спасибо страница за предложенный контент (вопрос, коммент, ссылка на youtube, ссылка на доп. контент)"""
    template_name = 'thx_data.html'


class MockView(ListView):
    """Список мок-интервью"""
    template_name = 'mock.html'
    model = MockInterview
    queryset = MockInterview.objects.filter(public=True)


def mock(request):
    profession_id = request.GET.get("profession")
    grade = request.GET.get("grade")
    if profession_id and grade:
        mocks = MockInterview.objects.filter(public=True, grade=grade, profession=profession_id)
    else:
        mocks = MockInterview.objects.filter(public=True)
    profs = Profession.objects.filter(public_mock=True)
    form_filter = MockForm
    return render(request, 'mock.html', {
        'mocks': mocks,
        'profs': profs,
        'form_filter': form_filter,
    })

