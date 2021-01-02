from IPython.display import HTML
from django.test import Client
from django.urls import reverse

c = Client()

url = reverse('api:test-items')
url = '/mymodel/'

HTML(c.get(url)).content.decode('utf8'))
