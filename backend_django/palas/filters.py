import django_filters
from .models import Pala

class PalaFilter(django_filters.FilterSet):
    precio_min = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio_max = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')
    peso_min = django_filters.NumberFilter(field_name='peso', lookup_expr='gte')
    peso_max = django_filters.NumberFilter(field_name='peso', lookup_expr='lte')
    año_lanzamiento_min = django_filters.NumberFilter(field_name='año_lanzamiento', lookup_expr='gte')
    año_lanzamiento_max = django_filters.NumberFilter(field_name='año_lanzamiento', lookup_expr='lte')

    class Meta:
        model = Pala
        fields = [
            'marca',
            'tienda',
            'forma',
            'nivel',
            'goma_nucleo',
            'balance',
            'genero',
        ]
