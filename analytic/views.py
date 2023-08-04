from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from rating.models import Profession


class ChoiceProfession(ListView):
    """Список профессий"""
    template_name = 'choice.html'
    model = Profession
    queryset = Profession.objects.filter(public_rating=True)



def analytic(request, prof_slug):
    return render(request, 'analytic.html')