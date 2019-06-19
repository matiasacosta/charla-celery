import os

"""
Configuracion de celery
"""

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ejemplo_celery.settings')

from django.conf import settings
from celery import Celery

app = Celery('ejemplo_celery',
             backend='rpc://',
             broker=f"amqp://{os.getenv('RABBITMQ_DEFAULT_USER', 'guest')}:{os.getenv('RABBITMQ_DEFAULT_PASS', 'guest')}@{os.getenv('RABBIT_HOST', 'localhost')}//")

# Lectura de la configuración de celery en el settings.py e.j.CELERY_ACCEPT_CONTENT = ['json']:
app.config_from_object('django.conf:settings')

# Permite descubrir las tareas en los modulos del proyecto, las tareas se buscaran en los archivos tasks.py.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)