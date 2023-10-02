from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views import View
from .service import giving_access


class ThxAccessSuccessView(TemplateView):
    """Страница об успешном получении доступа"""
    template_name = 'access_success.html'


class AccessView(View):
    def get(self, request):
        giving_access(request)
        return redirect('access_success')