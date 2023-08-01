from django.urls import path
from rating import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thx_data', views.thx_data, name='thx_data'),
    path('mock', views.mock, name='mock'),
    path('question/<int:question_id>', views.question, name='question'),
    path('quiz/<slug:prof_slug>', views.quiz, name='quiz'),
    path('<slug:prof_slug>', views.profession, name='profession'),
]