from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views import View
from .service import giving_access


class ThxAccessSuccessView(TemplateView):
    """Страница об успешном получении доступа"""
    template_name = 'access_success.html'


class ThxAccessSuccessOldView(TemplateView):
    """Страница об устаревшей ссылке"""
    template_name = 'access_success_old.html'


class AccessView(View):
    def get(self, request):
        giving_access(request)
        return redirect('access_success')


class AccessOldView(View):
    def get(self, request):
        giving_access(request)
        return redirect('access_success_old')
