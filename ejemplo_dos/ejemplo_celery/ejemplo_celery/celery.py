from __future__ import absolute_import
import os

"""
Configuracion de celery
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ejemplo_celery.settings')

from django.conf import settings
from celery import Celery

app = Celery('sueldos_ganancias',
             backend='amqp',
             broker=f"amqp://guest:guest@{os.getenv('RABBIT_HOST', 'localhost')}//")

# This reads, e.g., CELERY_ACCEPT_CONTENT = ['json'] from settings.py:
app.config_from_object('django.conf:settings')

# For autodiscover_tasks to work, you must define your tasks in a file called 'tasks.py'.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)