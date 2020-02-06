# from django.core import management
# management.call_command('makemigrations', 'myapp')
# management.call_command('migrate', 'myapp')

from django.db import connection

with connection.schema_editor() as schema_editor:
    schema_editor.create_model(MyModel)
