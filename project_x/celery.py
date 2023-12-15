from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_x.settings')

app = Celery('Data')
app.conf.timezone = 'Europe/Berlin'
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'fetch-forex-data': {
        'task': 'Data.tasks.fetch_forex_data',
        'schedule': crontab(minute='*'),
    },
}

app.conf.broker_connection_retry_on_startup = True
app.conf.beat_scheduler = 'celery.beat.PersistentScheduler'
app.conf.result_backend = 'rpc://'
