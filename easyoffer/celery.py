import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easyoffer.settings')

app = Celery('easyoffer')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'get_printer': {
#         'task': 'analytic.tasks.printer',
#         'schedule': crontab(minute='*/1')
#     },
# }
