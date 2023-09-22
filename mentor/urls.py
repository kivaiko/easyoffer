from django.urls import path
from mentor import views
from . import views
from mentor.views import ThxView, ThxReviewView

urlpatterns = [
    path('mentor', views.mentors, name='mentors'),
    path('mentor/thx', ThxView.as_view(), name='thx'),
    path('mentor/thx_review', ThxReviewView.as_view(), name='thx_review'),
    path('mentor/new_mentor', views.NewMentor.as_view(), name='new_mentor'),
    path('mentor/update/<int:pk>', views.MentorUpdate.as_view(), name='update_mentor'),
    path('mentor/<slug:username>', views.mentor, name='mentor')
]