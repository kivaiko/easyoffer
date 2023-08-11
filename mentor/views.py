from django.shortcuts import render
from django.views.generic import DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import *
from .forms import MentorForm, MentorFilterForm


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
    return render(request, 'mentor.html', {
        'mentor': mentor_detail,
    })


class NewMentor(CreateView):
    """Страница добавления нового ментора"""
    model = Mentor
    form_class = MentorForm
    template_name = 'new_mentor.html'
    success_url = reverse_lazy('thx')


class ThxView(TemplateView):
    """Страница с успешным добавлением нового ментора"""
    template_name = 'thx.html'
