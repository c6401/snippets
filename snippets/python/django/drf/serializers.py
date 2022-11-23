from rest_framework import serializers


class Serializer(serializers.ModelSerializer):
    name = serializers.CharField()
