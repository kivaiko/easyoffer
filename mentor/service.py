from .forms import ReviewForm
from .models import *
from django.db.models import Avg, Count, Q


def get_mentors_list(request):
    profession_id = request.GET.get("profession")
    topic_id = request.GET.get("topics")
    profession_filter = Q()
    if profession_id:
        profession_filter = Q(profession=profession_id)
    topic_filter = Q()
    if topic_id:
        topic_filter = Q(topics=topic_id)
    mentors_list = Mentor.objects.filter(public=True, permission=True).filter(
        profession_filter & topic_filter).annotate(avg=Avg('review__rating', filter=models.Q(review__public=True)),
                                                   review_count=Count('review', filter=models.Q(review__public=True)))
    return mentors_list


def get_mentor_data(username):
    mentor_detail = Mentor.objects.get(username=username)
    reviews = Review.objects.filter(mentor=mentor_detail, public=True)
    avg_rating = Review.objects.filter(mentor=mentor_detail, public=True).aggregate(Avg('rating'))
    return mentor_detail, reviews, avg_rating


def create_new_review(request, username):
    mentor_detail = Mentor.objects.get(username=username)
    form = ReviewForm(request.POST)
    if form.is_valid():
        Review.objects.create(
            mentor_id=mentor_detail.id,
            author=form.cleaned_data["author"],
            text=form.cleaned_data["text"],
            rating=form.cleaned_data["rating"]
        )