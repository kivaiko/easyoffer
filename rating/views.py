from django.shortcuts import render, redirect
from .forms import *
from .models import *


def index(request):
    professions = Profession.objects.filter(public_rating=True)
    return render(request, 'index.html', {'professions': professions})


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
    ratings = Rating.objects.select_related('question').filter(profession=prof_data, status='public').order_by("-rating")
    return render(request, 'profession.html', {
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
            Comment.objects.create(
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
    comments_count = Comment.objects.filter(question__id=question_data.id, status='public').count()
    best_short_comment = Comment.objects.filter(question__id=question_data.id, status='public').order_by("-short_rating").first()
    best_long_comment = Comment.objects.filter(question__id=question_data.id, status='public').order_by("-long_rating").first()
    if best_long_comment and best_short_comment:
        pass
    comments = Comment.objects.filter(question__id=question_data.id, status='public')
    any_comments = Comment.objects.filter(question__id=question_data.id, status='public').exclude(id=best_short_comment.id).exclude(id=best_long_comment.id).order_by("-short_rating").order_by("-long_rating")
    video_links = VideoAnswerLink.objects.filter(question__id=question_data.id, status='public')
    extra_links = ExtraContentLink.objects.filter(question__id=question_data.id, status='public')
    return render(request, 'question.html', {
        'comments_count': comments_count,
        'best_short_comment': best_short_comment,
        'best_long_comment': best_long_comment,
        'any_comments': any_comments,
        'comment_form': comment_form,
        'video_answer_form': video_answer_form,
        'extra_content_form': extra_content_form,
        'question_data': question_data,
        'comments': comments,
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
    ratings = Rating.objects.select_related('question').filter(profession=prof_data, status='public').order_by("-rating")
    return render(request, 'quiz.html', {
        'prof_data': prof_data,
        'ratings': ratings,
    })


def thx_data(request):
    return render(request, 'thx_data.html')


def mock(request):
    mocks = MockInterview.objects.filter(status=True)
    profs = Profession.objects.filter(public_rating=True)
    return render(request, 'mock.html', {
        'mocks': mocks,
        'profs': profs
    })
