import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easyoffer.settings')

app = Celery('easyoffer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get_analytic_from_hh': {
        'task': 'analytic.tasks.get_analytic_from_hh_api',
        'schedule': crontab(minute=0, hour=3),
    },
    'delete_access': {
        'task': 'access.tasks.delete_access_data',
        'schedule': crontab(minute=0, hour=2),

    }
}