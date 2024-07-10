import os
import django
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.wsgi')
application = get_wsgi_application()

ROOT_URLCONF = 'mysite.wsgi'
SECRET_KEY = 'secret'

def index(request):
    return django.http.HttpResponse('hello')

urlpatterns = [
    django.urls.path('', index),
]
