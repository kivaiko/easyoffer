from django.urls import path
from mentor import views
from . import views

urlpatterns = [
    path('mentor', views.mentors, name='mentors'),
    path('mentor/new_mentor', views.NewMentor.as_view(), name='new_mentor'),
    path('mentor/<slug:username>', views.mentor, name='mentor')
]