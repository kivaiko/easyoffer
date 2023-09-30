from django.urls import path
from mentor import views
from mentor.views import ThxView, ThxReviewView, MentorsListView, MentorView, NewMentor, MentorUpdate

urlpatterns = [
    path('mentor', MentorsListView.as_view(), name='mentors'),
    path('mentor/account', views.mentor_account, name='account'),
    path('mentor/thx', ThxView.as_view(), name='thx'),
    path('mentor/thx_review', ThxReviewView.as_view(), name='thx_review'),
    path('mentor/new_mentor', NewMentor.as_view(), name='new_mentor'),
    path('mentor/account/update', MentorUpdate.as_view(), name='update_mentor'),
    path('mentor/<slug:username>', MentorView.as_view(), name='mentor'),
]