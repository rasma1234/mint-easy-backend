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
    'fetch-forex-data1': {
        'task': 'Data.tasks.fetch_forex_data1',
        'schedule': crontab(minute='*'),
    },
    'fetch-forex-data2': {
        'task': 'Data.tasks.fetch_forex_data2',
        'schedule': crontab(minute='*'),
    },
    'fetch-forex-data3': {
        'task': 'Data.tasks.fetch_forex_data3',
        'schedule': crontab(minute='*'),
    },
    'fetch-forex-data4': {
        'task': 'Data.tasks.fetch_forex_data4',
        'schedule': crontab(minute='*'),
    },
    'fetch-crypto-data': {
        'task': 'Data.tasks.fetch_crypto_data',
        'schedule': crontab(minute='*'),
    },
    'fetch-crypto-data1': {
        'task': 'Data.tasks.fetch_crypto_data1',
        'schedule': crontab(minute='*'),
    },
    'fetch-stock-data': {
        'task': 'Data.tasks.fetch_stock_data',
        'schedule': crontab(minute='*'),
    },
    'fetch-stock-data1': {
        'task': 'Data.tasks.fetch_stock_data1',
        'schedule': crontab(minute='*'),
    },
    'fetch-stock-data2': {
        'task': 'Data.tasks.fetch_stock_data2',
        'schedule': crontab(minute='*'),
    },
    'fetch-stock-data3': {
        'task': 'Data.tasks.fetch_stock_data3',
        'schedule': crontab(minute='*'),
    },
    'fetch-stock-data4': {
        'task': 'Data.tasks.fetch_stock_data4',
        'schedule': crontab(minute='*'),
    },
    'fetch-forex-data-15': {
        'task': 'Data.tasks.fetch_forex_data_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-forex-data1-15': {
        'task': 'Data.tasks.fetch_forex_data1_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-forex-data2-15': {
        'task': 'Data.tasks.fetch_forex_data2_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-forex-data3-15': {
        'task': 'Data.tasks.fetch_forex_data3_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-forex-data4-15': {
        'task': 'Data.tasks.fetch_forex_data4_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-crypto-data-15': {
        'task': 'Data.tasks.fetch_crypto_data_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-crypto-data1-15': {
        'task': 'Data.tasks.fetch_crypto_data1_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-stock-data-15': {
        'task': 'Data.tasks.fetch_stock_data_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-stock-data1-15': {
        'task': 'Data.tasks.fetch_stock_data1_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-stock-data2-15': {
        'task': 'Data.tasks.fetch_stock_data2_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-stock-data3-15': {
        'task': 'Data.tasks.fetch_stock_data3_15',
        'schedule': crontab(minute='*'),
    },
    'fetch-stock-data4-15': {
        'task': 'Data.tasks.fetch_stock_data4_15',
        'schedule': crontab(minute='*'),
    },
 }
app.conf.broker_connection_retry_on_startup = True
app.conf.beat_scheduler = 'celery.beat.PersistentScheduler'
app.conf.result_backend = 'rpc://'