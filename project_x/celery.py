# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# setze das Standard-Django-Einstellungsmodul für das 'celery' Programm.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_x.settings')

# erstelle eine Celery-Instanz und konfiguriere sie mit den Einstellungen von Django
app = Celery('Data')

# Verwende hier einen String, der dem Muster deines Projekts entspricht
app.config_from_object('django.conf:settings', namespace='CELERY')

# Lade Aufgabenmodule aus allen registrierten Django-App-Konfigurationen.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Konfiguriere Celery Beat, um periodische Aufgaben zu planen
app.conf.beat_schedule = {
    'fetch-forex-data': {
        'task': '/home/dci-student/Smart_Invest/Data/views.py',
        'schedule': crontab(minute='*'),  # Hier kannst du die Planung anpassen (z.B. täglich um Mitternacht)
    },
}
