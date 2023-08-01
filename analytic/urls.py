from django.urls import path
from analytic import views

urlpatterns = [
    path('analytic', views.choice, name='choice'),
    path('analytic/<slug:prof_slug>', views.analytic, name='analytic')
]

