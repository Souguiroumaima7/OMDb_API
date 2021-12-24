import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OMDb_API.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")

app = Celery("OMDb_API")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
