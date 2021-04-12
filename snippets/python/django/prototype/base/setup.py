# !mkdir -p /tmp/myapp/myapp
# %cd /tmp/myapp

import os
import sys
import django
from django.conf import settings

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

urlpatterns = []

settings.configure(
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
            # 'NAME': 'test.sqlite3',
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
        # 'django.contrib.auth',
        # 'django.contrib.contenttypes',
        # 'django.contrib.sessions',
        # 'django.contrib.messages',
        # 'django.contrib.admin',
        # 'django.contrib.staticfiles',
        # 'rest_framework',
        # 'test.django',
        # 'django_filters',
        # 'myapp',
    ),
    # MIDDLEWARE = (
    #     'django.contrib.sessions.middleware.SessionMiddleware',
    #     'django.contrib.auth.middleware.AuthenticationMiddleware',
    #     'django.contrib.messages.middleware.MessageMiddleware',
    # ),
    # ROOT_URLCONF=sys.modules[__name__],
    # ALLOWED_HOSTS = ['*'],
    # STATIC_URL = '/static/',
    # STATIC_ROOT = 'static/',
    # TEMPLATES = [
    #     {
    #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #         'DIRS': [],
    #         'APP_DIRS': True,
    #         'OPTIONS': {
    #             'context_processors': [
    #                 'django.template.context_processors.debug',
    #                 'django.template.context_processors.request',
    #                 'django.contrib.auth.context_processors.auth',
    #                 'django.contrib.messages.context_processors.messages',
    #             ],
    #         },
    #     },
    # ],
    # SECRET_KEY = '!@#$%^&*()',
    DEBUG=True,
)
django.setup()
# %%
