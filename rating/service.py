from .forms import AddQuestion, QuestionSearchForm
from .models import Access, Profession, Rating, MockInterview
from django.utils import timezone
from django.db.models import F, Q
from django.core.paginator import Paginator


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_access_status(request):
    ip = get_client_ip(request)
    return Access.objects.filter(ip_address=ip).exists()


def delete_access():
    current_date = timezone.now()
    filtered_records = Access.objects.filter(delete_date__lt=current_date)
    filtered_records.delete()
    print('delete_access – отработала')


def func(slug):
    prof_data = Profession.objects.get(slug=slug)
    available_tags = prof_data.tags.all()
    questions_amount = Rating.objects.select_related('question').filter(profession=prof_data, public=True).count()
    return prof_data, available_tags, questions_amount


def get_ratings(tag, search_form, prof_data):
    if tag and tag != 'Все':
        ratings = Rating.objects.select_related('question').filter(profession=prof_data, public=True,
                                                                   question__tag__title=tag).order_by(
            "-rating") \
            .annotate(chance=F('rating') * 100 / prof_data.votes)
    else:
        ratings = Rating.objects.select_related('question').filter(profession=prof_data, public=True).order_by(
            "-rating") \
            .annotate(chance=F('rating') * 100 / prof_data.votes)
    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        if search_query:
            ratings = ratings.filter(question__title__icontains=search_query)
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
    mocks = MockInterview.objects.filter(public=True).filter(profession_filter & grade_filter)
    return mocks, profession_id, grade


def get_pagination(request, queryset):
    paginator = Paginator(queryset, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

