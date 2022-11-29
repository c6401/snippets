"""MyModel Serializer."""
from rest_framework import serializers

from . import models


class MyModelSerializer(serializers.ModelSerializer):
    """MyModel serializer"""

    class Meta:
        model = models.MyModel
        fields = '__all__'
