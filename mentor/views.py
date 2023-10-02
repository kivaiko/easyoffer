from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from django.views import View
from .forms import MentorForm, MentorFilterForm, ReviewForm
from .service import get_mentors_list, get_mentor_data, create_new_review
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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


@method_decorator(login_required, name='dispatch')
class NewMentor(CreateView):
    """Страница добавления нового ментора"""
    model = Mentor
    form_class = MentorForm
    template_name = 'mentor_edit.html'
    success_url = reverse_lazy('thx')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MentorUpdate(LoginRequiredMixin, UpdateView):
    """Страница обновления данных ментора"""
    model = User
    form_class = MentorForm
    template_name = 'mentor_edit.html'
    success_url = reverse_lazy('mentors')

    def get_object(self, queryset=None):
        return self.request.user.mentor


class ThxView(TemplateView):
    """Страница с успешным добавлением нового ментора"""
    template_name = 'thx.html'


class ThxReviewView(TemplateView):
    """Страница с успешным добавлением нового отзыва"""
    template_name = 'thx_review.html'


def mentor_account(request):
    user = request.user
    mentor = Mentor.objects.filter(user=user).first()
    if mentor is not None:
        return redirect('update_mentor')
    else:
        return render(request, 'account.html')