from django.shortcuts import render
from .models import *


def mentors(request):
    mentors_list = Mentor.objects.filter(public=True)
    return render(request, 'mentors.html', {'mentors': mentors_list})


def mentor(request, username):
    return render(request, 'mentor.html')