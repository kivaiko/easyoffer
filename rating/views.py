from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.db.models import F, Value, Q
from django.core.paginator import Paginator
from .forms import *
from .models import *
from .service import get_access_status, get_client_ip, get_prof_data, get_ratings, get_filtered_mocks, get_pagination, \
    get_question_content, create_answer, create_video_link, create_extra_link, get_data_from_content_form, \
    update_rating_from_quiz, create_mock, crete_question, giving_access


class IndexView(ListView):
    """Список профессий"""
    template_name = 'index.html'
    model = Profession
    queryset = Profession.objects.filter(public_rating=True)


def profession(request, slug):
    if request.method == "POST":
        form = AddQuestion(request.POST)
        if form.is_valid():
            crete_question(form, slug)
            return redirect('thx_data')

    tag = request.GET.get("tag")
    search_form, add_question_form = QuestionSearchForm(request.GET), AddQuestion()
    prof_data, available_tags, questions_amount = get_prof_data(slug)
    ratings = get_ratings(tag, search_form, prof_data)
    access_status = get_access_status(request)
    page_obj = get_pagination(request, ratings)
    return render(request, 'question_rating.html', {
        'prof_data': prof_data,
        'available_tags': available_tags,
        'ratings': ratings,
        'questions_amount': questions_amount,
        'page_obj': page_obj,
        'form': add_question_form,
        'search_form': search_form,
        'access': access_status,
        'tag': tag,
    })


def question(request, question_id):
    if request.method == "POST":
        comment_form, video_form, extra_content_form = get_data_from_content_form(request)
        if comment_form.is_valid():
            create_answer(question_id, comment_form)
            return redirect('thx_data')
        if video_form.is_valid():
            create_video_link(question_id, video_form)
            return redirect('thx_data')
        if extra_content_form.is_valid():
            create_extra_link(question_id, extra_content_form)
            return redirect('thx_data')

    comment_form, video_answer_form, extra_content_form = CommentForm(), VideoAnswerForm(prefix='video'),\
                                                          ExtraContentForm(prefix='content')
    question_data, answers, video_links, extra_links = get_question_content(question_id)
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
        update_rating_from_quiz(request, prof_slug)
        return redirect('thx_quiz')
    prof_data = Profession.objects.get(slug=prof_slug)
    ratings = Rating.objects.select_related('question').filter(profession=prof_data, public=True).order_by("-rating")
    return render(request, 'quiz.html', {
        'prof_data': prof_data,
        'ratings': ratings,
    })


class ThxQuizView(TemplateView):
    """Спасибо страница за участие в опросе"""
    template_name = 'thx_quiz.html'


class ThxView(TemplateView):
    """Спасибо страница за предложенный контент (вопрос, коммент, ссылка на youtube, ссылка на доп. контент)"""
    template_name = 'thx_data.html'


class ThxAccessSuccessView(TemplateView):
    """Страница об успешном получении доступа"""
    template_name = 'access_success.html'


class MockView(ListView):
    """Список мок-интервью"""
    template_name = 'mock.html'
    model = MockInterview
    queryset = MockInterview.objects.filter(public=True)


def mock(request):
    if request.method == "POST":
        form = AddMockForm(request.POST)
        if form.is_valid():
            create_mock(form)
            return redirect('thx_data')
    mocks, profession_id, grade = get_filtered_mocks(request)
    page_obj = get_pagination(request, mocks)
    form_filter, form = MockFilterForm, AddMockForm
    return render(request, 'mock.html', {
        'mocks': mocks,
        'page_obj': page_obj,
        'form_filter': form_filter,
        'form': form,
        'profession_id': profession_id,
        'grade': grade,
    })


def access(request):
    giving_access(request)
    return redirect('access_success')
