from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.views import View
from .models import *
from .forms import MentorForm


def mentors(request):
    mentors_list = Mentor.objects.filter(public=True)
    return render(request, 'mentors.html', {'mentors': mentors_list})


def mentor(request, username):
    mentor_detail = Mentor.objects.get(username=username)
    return render(request, 'mentor.html', {
        'mentor': mentor_detail,
    })


class NewMentor(CreateView):
    model = Mentor
    form_class = MentorForm
    template_name = 'new_mentor.html'