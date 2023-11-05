from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views import View
from .forms import *
from .models import *
from access.service import get_access_status
from .service import get_prof_data, get_ratings, get_filtered_mocks, get_pagination, \
    get_question_content, create_answer, create_video_link, create_extra_link, get_data_from_content_form, \
    update_rating_from_quiz, create_mock, crete_question


class IndexView(ListView):
    """Список профессий"""
    template_name = 'index.html'
    model = Profession
    queryset = Profession.objects.filter(public_rating=True).order_by('title')


class ProfessionView(View):
    def post(self, request, slug):
        form = AddQuestion(request.POST)
        if form.is_valid():
            crete_question(form, slug)
            return redirect('thx_data')

    def get(self, request, slug):
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


class QuestionView(View):
    def post(self, request, question_id):
        comment_form, video_form, extra_content_form = get_data_from_content_form(request)
        redirect_target = 'thx_data'
        if comment_form.is_valid():
            create_answer(question_id, comment_form)
        elif video_form.is_valid():
            create_video_link(question_id, video_form)
        elif extra_content_form.is_valid():
            create_extra_link(question_id, extra_content_form)
        else:
            redirect_target = 'error'
        return redirect(redirect_target)

    def get(self, request, question_id):
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


class QuizView(View):
    def post(self, request, slug):
        update_rating_from_quiz(request, slug)
        return redirect('thx_quiz')

    def get(self, request, slug):
        prof_data = Profession.objects.get(slug=slug)
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


class ErrorView(TemplateView):
    """Страница ошибки"""
    template_name = 'error.html'


class MockView(View):
    def post(self, request):
        form = AddMockForm(request.POST)
        if form.is_valid():
            create_mock(form)
            return redirect('thx_data')

    def get(self, request):
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