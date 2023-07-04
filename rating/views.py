from django.shortcuts import render
from .models import Profession, Question, Comment, Link


def index(request):
    professions = Profession.objects.all()
    return render(request, 'index.html', {'professions': professions})


def profession(request, prof_slug):
    prof_data = Profession.objects.get(prof_slug=prof_slug)
    questions = Question.objects.filter(profession__id=prof_data.id).order_by("-rating_qty")
    return render(request, 'profession.html', {
        'prof_data': prof_data,
        'questions': questions,
    })


def question(request, question_id):
    question_data = Question.objects.get(id=question_id)
    comments = Comment.objects.filter(question__id=question_data.id)
    links = Link.objects.filter(question__id=question_data.id).order_by("-rating_qty")
    return render(request, 'question.html', {
        'question_data': question_data,
        'comments': comments,
        'links': links
    })



