from django.apps import apps
from django.db import models

if apps.all_models['myapp']:
    del apps.all_models['myapp']['mymodel']


class MyModel(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        app_label = 'myapp'

# from django.core.management import call_command
# call_command('makemigrations', 'myapp')
# call_command('migrate', 'myapp')

from django.db import connection

with connection.schema_editor() as schema_editor:
    schema_editor.create_model(MyModel)
