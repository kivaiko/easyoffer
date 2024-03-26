from django.urls import path
from access.views import ThxAccessSuccessView, AccessView, ThxAccessSuccessOldView, AccessOldView

urlpatterns = [
    path('access_success', ThxAccessSuccessView.as_view(), name='access_success'),
    path('access_old', ThxAccessSuccessOldView.as_view(), name='access_old'),
    path('NDTOIzOclYmcKzvzWAJVlYmcKzvOclDTO', AccessView.as_view(), name='access'),
    path('Jljo0U9Erg7QDtkb133G7vzDexHVw6Iz', AccessOldView.as_view(), name='access_old'),
]
