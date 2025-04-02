# palas/filters.py
import django_filters
from .models import Pala

class PalaFilter(django_filters.FilterSet):
    precio_min = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio_max = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')

    class Meta:
        model = Pala
        fields = ['marca', 'tienda', 'precio_min', 'precio_max']
