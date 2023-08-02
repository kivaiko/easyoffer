from django.urls import path
from rating import views
from rating.views import IndexView, ThxView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('thx_data', ThxView.as_view(), name='thx_data'),
    path('mock', views.mock, name='mock'),
    path('question/<int:question_id>', views.question, name='question'),
    path('quiz/<slug:prof_slug>', views.quiz, name='quiz'),
    path('rating/<slug:prof_slug>', views.profession, name='question_rating'),
]