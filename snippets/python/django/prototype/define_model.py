from django.apps import apps
from django.db import models

if apps.all_models['myapp']:
    del apps.all_models['myapp']['mymodel']


class MyModel(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        app_label = 'myapp'
