from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from rating.models import Profession
from rating.service import get_access_status


class ChoiceProfession(ListView):
    """Список профессий"""
    template_name = 'choice.html'
    model = Profession
    queryset = Profession.objects.filter(public_analytic=True)


def analytic(request, slug):
    title = request.GET.get("title")
    prof_data = Profession.objects.get(slug=slug)
    all_searches = Search.objects.filter(profession=prof_data)
    access_status = get_access_status(request)
    if title:
        search = Search.objects.get(profession=prof_data, title=title)
    else:
        search = Search.objects.get(profession=prof_data, title='Все')
    skills = Skill.objects.filter(search=search)
    keywords = KeyWord.objects.filter(search=search)
    return render(request, 'analytic.html', {
        'search': search,
        'skills': skills,
        'keywords': keywords,
        'all_searches': all_searches,
        'access': access_status,
    })