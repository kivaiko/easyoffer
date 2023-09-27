from django.urls import path
from analytic.views import ChoiceProfession, SearchAnalytic

urlpatterns = [
    path('analytic', ChoiceProfession.as_view(), name='choice'),
    path('analytic/<slug:slug>', SearchAnalytic.as_view(), name='analytic')
]

