from datetime import datetime, timedelta
from django.utils import timezone
from .models import Access


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


def giving_access(request):
    ip = get_client_ip(request)
    if not Access.objects.filter(ip_address=ip).exists():
        current_datetime = datetime.now()
        new_datetime = current_datetime + timedelta(days=30)
        print(new_datetime)
        Access.objects.create(
            ip_address=ip,
            delete_date=new_datetime,
        )