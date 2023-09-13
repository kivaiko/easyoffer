from .models import Access
from django.utils import timezone


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_access_status(ip):
    return Access.objects.filter(ip_address=ip).exists()


def delete_access():
    current_date = timezone.now()
    filtered_records = Access.objects.filter(delete_date__lt=current_date)
    filtered_records.delete()
    print('delete_access – отработала')