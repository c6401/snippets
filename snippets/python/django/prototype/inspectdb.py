import os
import sys
from io import StringIO
from types import SimpleNamespace
from urllib.parse import urlparse

import django
from django.conf import settings
from django.core.management import call_command

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

location = urlparse('...')

engine = {
    # 'sqlite3': 'django.db.backends.sqlite3',
    'postgresql': 'django.db.backends.postgresql',
}[location.scheme]

settings.configure(
    DATABASES = {
        'default': {
            'ENGINE': engine, 'USER': location.username,
            'NAME': location.path[1:], 'PASSWORD': location.password,
            'HOST': location.hostname, 'PORT': location.port,
        },
    },
)
django.setup()

text = StringIO()
call_command('inspectdb', stdout=text)
inspected = text.getvalue()
inspected = inspected.replace(
    "    class Meta:\n",
    "    class Meta:\n        app_label = 'default'\n"
)
models = SimpleNamespace()
exec(inspected, vars(models))
