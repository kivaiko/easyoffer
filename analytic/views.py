from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from rating.models import Profession
from rating.service import get_access_status, get_client_ip


class ChoiceProfession(ListView):
    """Список профессий"""
    template_name = 'choice.html'
    model = Profession
    queryset = Profession.objects.filter(public_analytic=True)


def analytic(request, prof_slug):
    title = request.GET.get("title")
    prof_data = Profession.objects.get(prof_slug=prof_slug)
    all_searches = Search.objects.filter(profession=prof_data)
    ip = get_client_ip(request)
    access = get_access_status(ip)
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
        'access': access,
    })