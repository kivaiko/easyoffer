from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from rating.models import Profession
from access.service import get_access_status
from .service import get_search_data


class ChoiceProfession(ListView):
    """Список профессий"""
    template_name = 'choice.html'
    model = Profession
    queryset = Profession.objects.filter(public_analytic=True).order_by('title')


class SearchAnalytic(View):
    def post(self, request, slug):
        pass

    def get(self, request, slug):
        search, skills, keywords, searches_for_prof = get_search_data(request, slug)
        access_status = get_access_status(request)
        return render(request, 'analytic.html', {
            'search': search,
            'skills': skills,
            'keywords': keywords,
            'all_searches': searches_for_prof,
            'access': access_status,
        })