from django.http import HttpResponse

urlpatterns = [
    url(r'^ping', lambda r: HttpResponse('pong')),
