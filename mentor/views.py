from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import MentorForm, MentorFilterForm, ReviewForm
from django.db.models import Avg, Count, Q


def mentors(request):

    profession_id = request.GET.get("profession")
    topic_id = request.GET.get("topics")
    profession_filter = Q()
    if profession_id:
        profession_filter = Q(profession=profession_id)
    topic_filter = Q()
    if topic_id:
        topic_filter = Q(topics=topic_id)
    mentors_list = Mentor.objects.filter(public=True, permission=True).filter(profession_filter & topic_filter).annotate(avg=Avg('review__rating', filter=models.Q(review__public=True)), review_count=Count('review', filter=models.Q(review__public=True)))

    # mentors_list = Mentor.objects.filter(public=True, permission=True).annotate(avg=Avg('review__rating', filter=models.Q(review__public=True)), review_count=Count('review', filter=models.Q(review__public=True)))
    form = MentorFilterForm()
    return render(request, 'mentors.html', {
        'mentors': mentors_list,
        'form': form,
    })


def mentor(request, username):
    mentor_detail = Mentor.objects.get(username=username)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                mentor_id=mentor_detail.id,
                author=form.cleaned_data["author"],
                text=form.cleaned_data["text"],
                rating=form.cleaned_data["rating"]
            )
            return redirect('thx_review')
    reviews = Review.objects.filter(mentor=mentor_detail, public=True)
    avg_rating = Review.objects.filter(mentor=mentor_detail, public=True).aggregate(Avg('rating'))
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
