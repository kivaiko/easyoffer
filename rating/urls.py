from django.urls import path
from rating.views import IndexView, ThxView, ThxQuizView, ProfessionView, QuestionView, QuizView,\
    MockView, ErrorView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('thx_data', ThxView.as_view(), name='thx_data'),
    path('error', ErrorView.as_view(), name='error'),
    path('mock', MockView.as_view(), name='mock'),
    path('question/<int:question_id>', QuestionView.as_view(), name='question'),
    path('quiz/thx_quiz', ThxQuizView.as_view(), name='thx_quiz'),
    path('quiz/<slug:slug>', QuizView.as_view(), name='quiz'),
    path('rating/<slug:slug>', ProfessionView.as_view(), name='question_rating'),
]