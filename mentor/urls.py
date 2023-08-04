from django.urls import path
from mentor import views

urlpatterns = [
    path('mentor', views.mentors, name='mentors'),
    path('mentor/<slug:username>', views.mentor, name='mentor')
]