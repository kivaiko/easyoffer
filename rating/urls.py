from django.urls import path
from rating import views
from rating.views import IndexView, ThxView, ThxQuizView, ThxAccessSuccessView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('thx_data', ThxView.as_view(), name='thx_data'),
    path('access_success', ThxAccessSuccessView.as_view(), name='access_success'),
    path('mock', views.mock, name='mock'),
    path('access', views.access, name='access'),
    path('question/<int:question_id>', views.question, name='question'),
    path('quiz/thx_quiz', ThxQuizView.as_view(), name='thx_quiz'),
    path('quiz/<slug:prof_slug>', views.quiz, name='quiz'),
    path('rating/<slug:slug>', views.profession, name='question_rating'),
]