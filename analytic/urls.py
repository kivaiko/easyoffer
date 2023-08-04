from django.urls import path
from analytic import views
from analytic.views import ChoiceProfession

urlpatterns = [
    path('analytic', ChoiceProfession.as_view(), name='choice'),
    path('analytic/<slug:prof_slug>', views.analytic, name='analytic')
]

