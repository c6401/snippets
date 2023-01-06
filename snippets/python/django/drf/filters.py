import django_filters

from .models import Model


class Filter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Model
        fields = ['name', 'description']
