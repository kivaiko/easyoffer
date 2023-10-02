from django.urls import path
from access.views import ThxAccessSuccessView, AccessView

urlpatterns = [
    path('access_success', ThxAccessSuccessView.as_view(), name='access_success'),
    path('Jljo0U9Erg7QDtkb133G7vzDexHVw6Iz', AccessView.as_view(), name='access'),
]