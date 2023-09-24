from django.urls import path
from rating import views
from rating.views import IndexView, ThxView, ThxQuizView, ThxAccessSuccessView, ProfessionView, QuestionView, QuizView,\
    MockView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('thx_data', ThxView.as_view(), name='thx_data'),
    path('access_success', ThxAccessSuccessView.as_view(), name='access_success'),
    path('mock', MockView.as_view(), name='mock'),
    path('access', views.access, name='access'),
    path('question/<int:question_id>', QuestionView.as_view(), name='question'),
    path('quiz/thx_quiz', ThxQuizView.as_view(), name='thx_quiz'),
    path('quiz/<slug:prof_slug>', QuizView.as_view(), name='quiz'),
    path('rating/<slug:slug>', ProfessionView.as_view(), name='question_rating'),
]