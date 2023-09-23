from django.urls import path
from . import views

urlpatterns = [
    path('user/register', views.register, name='register'),
    path('user/login', views.user_login, name='login'),
    path('user/oauth', views.oauth, name='oauth'),
]