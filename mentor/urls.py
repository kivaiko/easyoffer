from django.urls import path
from mentor import views

urlpatterns = [
    path('mentor', views.mentors, name='mentors'),
    path('mentor/<username>', views.mentor, name='mentor')
]