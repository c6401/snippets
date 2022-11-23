"""MyModelViewset."""
from rest_framework import viewsets

from . import models
from . import serializers


class MyModelViewset(viewsets.ModelViewSet):
    """MyModelViewset."""

    queryset = models.MyModel.objects.all()
    serializer_class = serializers.MyModelSerializer
