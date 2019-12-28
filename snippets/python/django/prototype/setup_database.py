import sys
import django
from django.conf import settings

urlpatterns = []

settings.configure(
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'test.sqlite3',
        },
        # 'default': {
        #     'ENGINE': 'django.db.backends.postgresql',
        #     'USER': 'postgres',
        #     'NAME': 'postgres',
        #     'PASSWORD': 'postgres',
        #     'HOST': '127.0.0.1',
        #     'PORT': '5432'
        # },
    },
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        # 'rest_framework',
        # 'test.django',
        # 'django_filters',
    ),
    ROOT_URLCONF=sys.modules[__name__],
    ALLOWED_HOSTS = ['*'],
    DEBUG=True,
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ],
    # SECRET_KEY = '!@#$%^&*()',
)
django.setup()
