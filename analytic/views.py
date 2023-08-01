from django.shortcuts import render
from .models import *
from rating.models import Profession


def choice(request):
    return render(request, 'choice.html')


def analytic(request, prof_slug):
    return render(request, 'analytic.html')