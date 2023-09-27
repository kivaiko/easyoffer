from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from django.views import View
from .forms import MentorForm, MentorFilterForm, ReviewForm
from .service import get_mentors_list, get_mentor_data, create_new_review


class MentorsListView(View):
    def get(self, request):
        mentors_list = get_mentors_list(request)
        form = MentorFilterForm()
        return render(request, 'mentors.html', {
            'mentors': mentors_list,
            'form': form,
        })


class MentorView(View):
    def post(self, request, username):
        create_new_review(request, username)
        return redirect('thx_review')

    def get(self, request, username):
        mentor_detail, reviews, avg_rating = get_mentor_data(username)
        review_form = ReviewForm()
        return render(request, 'mentor.html', {
            'mentor': mentor_detail,
            'reviews': reviews,
            'avg_rating': avg_rating,
            'form': review_form,
        })


class NewMentor(CreateView):
    """Страница добавления нового ментора"""
    model = Mentor
    form_class = MentorForm
    template_name = 'new_mentor.html'
    success_url = reverse_lazy('thx')


class MentorUpdate(UpdateView):
    """Страница обновления данных ментора"""
    model = Mentor
    form_class = MentorForm
    template_name = 'mentor_edit.html'
    success_url = reverse_lazy('mentors')
    slug_url_kwarg = 'username'
    slug_field = 'username'


class ThxView(TemplateView):
    """Страница с успешным добавлением нового ментора"""
    template_name = 'thx.html'


class ThxReviewView(TemplateView):
    """Страница с успешным добавлением нового отзыва"""
    template_name = 'thx_review.html'
