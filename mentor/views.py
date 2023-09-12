from django.shortcuts import render
from django.views.generic import DetailView, CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import MentorForm, MentorFilterForm
from django.db.models import Avg


def mentors(request):
    direction = request.GET.get("directions")
    topic = request.GET.get("topics")
    if direction and topic:
        mentors_list = Mentor.objects.filter(public=True, topics=topic, directions=direction)
    else:
        mentors_list = Mentor.objects.filter(public=True)
    form = MentorFilterForm
    return render(request, 'mentors.html', {
        'mentors': mentors_list,
        'form': form,
    })


def mentor(request, username):
    mentor_detail = Mentor.objects.get(username=username)
    reviews = Review.objects.filter(mentor=mentor_detail)
    avg_rating = Review.objects.filter(mentor=mentor_detail).aggregate(Avg('rating'))
    return render(request, 'mentor.html', {
        'mentor': mentor_detail,
        'reviews': reviews,
        'avg_rating': avg_rating,
    })


class NewMentor(CreateView):
    """Страница добавления нового ментора"""
    model = Mentor
    form_class = MentorForm
    template_name = 'new_mentor.html'
    success_url = reverse_lazy('thx')


class MentorUpdate(UpdateView):
    """Страница обновления данных ментора"""
    model = Mentor
    form_class = MentorForm
    template_name = 'mentor_edit.html'
    success_url = reverse_lazy('mentors')


class ThxView(TemplateView):
    """Страница с успешным добавлением нового ментора"""
    template_name = 'thx.html'
