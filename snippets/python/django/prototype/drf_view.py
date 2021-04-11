from django.urls import path
from rest_framework import views
from rest_framework.response import Response


class MyView(views.APIView):
    def get(self, request, format=None):
        return Response({'test': 'test'})


mypath = path('myview', MyView.as_view())
if urlpatterns:
    urlpatterns[0] = mypath
else:
    urlpatterns.append(mypath)

# from django.core.management import call_command
# call_command('collectstatic', '--noinput')
