from django.contrib import admin
from django.urls import path
from rating import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('question/<int:question_id>', views.question, name='question'),
    path('<slug:prof_slug>', views.profession, name='profession'),
]
