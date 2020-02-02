from IPython.display import HTML
from django.test import Client

c = Client()

HTML(c.get('/mymodel/').content.decode('utf8'))
