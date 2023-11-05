from .forms import CommentForm, VideoAnswerForm, ExtraContentForm
from .models import Profession, Rating, MockInterview, Question, Answer, VideoAnswerLink, ExtraContentLink
from django.db.models import F, Q
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404


def get_prof_data(slug):
    prof_data = Profession.objects.prefetch_related('tags').get(slug=slug)
    questions_amount = Rating.objects.select_related('question').filter(profession=prof_data, public=True).count()
    return prof_data, prof_data.tags.all(), questions_amount


def get_ratings(tag, search_form, prof_data):
    ratings = Rating.objects.select_related('question__tag').filter(profession=prof_data, public=True)
    if tag and tag != 'Все':
        ratings = ratings.filter(question__tag__title=tag)
    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        if search_query:
            ratings = ratings.filter(Q(question__title__icontains=search_query))
    ratings = ratings.order_by("-rating").annotate(chance=F('rating') * 100 / prof_data.votes)
    return ratings


def get_filtered_mocks(request):
    profession_id = request.GET.get("profession")
    grade = request.GET.get("grade")
    profession_filter = Q()
    if profession_id:
        profession_filter = Q(profession=profession_id)
    grade_filter = Q()
    if grade:
        grade_filter = Q(grade=grade)
    mocks = MockInterview.objects.filter(public=True).filter(profession_filter & grade_filter).select_related('profession')
    return mocks, profession_id, grade


def get_pagination(request, queryset):
    paginator = Paginator(queryset, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_question_content(question_id):
    question_data = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question__id=question_data.id, public=True).order_by("-rating")
    video_links = VideoAnswerLink.objects.filter(question__id=question_data.id, public=True)
    extra_links = ExtraContentLink.objects.filter(question__id=question_data.id, public=True)
    return question_data, answers, video_links, extra_links


def get_data_from_content_form(request):
    comment_form = CommentForm(request.POST)
    video_form = VideoAnswerForm(request.POST, prefix='video')
    extra_content_form = ExtraContentForm(request.POST, prefix='content')
    return comment_form, video_form, extra_content_form


def create_answer(question_id, form):
    Answer.objects.create(
        question_id=question_id,
        text=form.cleaned_data["text"],
        author=form.cleaned_data["author"],
        url=form.cleaned_data["url"]
    )


def create_video_link(question_id, form):
    VideoAnswerLink.objects.create(
        question_id=question_id,
        title=form.cleaned_data["title"],
        url=form.cleaned_data["url"]
    )


def create_extra_link(question_id, form):
    ExtraContentLink.objects.create(
        question_id=question_id,
        title=form.cleaned_data["title"],
        url=form.cleaned_data["url"]
    )


def create_mock(form):
    MockInterview.objects.create(
        profession=form.cleaned_data["profession"],
        title=form.cleaned_data["title"],
        url=form.cleaned_data["url"],
        grade=form.cleaned_data["grade"]
    )


def crete_question(form, slug):
    Question.objects.create(
        title=form.cleaned_data["title"],
        tag=form.cleaned_data["tag"]
    )
    Rating.objects.create(
        profession=Profession.objects.get(slug=slug),
        question=Question.objects.latest('id'),
    )


def update_rating_from_quiz(request, slug):
    question_ids_to_update = []

    for i, value in request.POST.items():
        if value == "Встречался":
            question_ids_to_update.append(i)

    if question_ids_to_update:
        Rating.objects.filter(id__in=question_ids_to_update).update(rating=F('rating') + 1)

    profession_votes = get_object_or_404(Profession, slug=slug)
    profession_votes.votes += 1
    profession_votes.save()