#manage.py makemigrations --empty yourappname
from django.db import migrations

def migrate(apps, schema_editor):
    """???"""
    MyModel = apps.get_model('yourappname', 'MyModel')

class Migration(migrations.Migration):

    dependencies = [
        ('yourappname', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate),
    ]

