import json
from django.conf import settings
from django.http import HttpResponse
from ruamel import yaml

urlpatterns = [
    url(r'^debug', lambda r: HttpResponse('<pre>' + yaml.dump(json.loads(json.dumps({'request': r.__dict__, 'settings': settings.__dict__}, default=str)), default_flow_style=False))),
