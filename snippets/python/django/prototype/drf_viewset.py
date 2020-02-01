import django_filters
from django.urls import path, include
from rest_framework import serializers
from rest_framework.routers import DefaultRouter


class MyModelFilter(django_filters.FilterSet):
    class Meta:
        model = MyModel
        fields = '__all__'


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    filter_class = MyModelFilter


router = DefaultRouter()
router.register('mymodel', MyModelViewSet)
mypath = path('', include(router.urls))

urlpatterns.append(mypath)
