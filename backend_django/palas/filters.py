import django_filters
from .models import Pala
from django.db.models import Q

class PalaFilter(django_filters.FilterSet):
    # Rango de precio
    precio_min = django_filters.NumberFilter(field_name='precio', lookup_expr='gte')
    precio_max = django_filters.NumberFilter(field_name='precio', lookup_expr='lte')

    # Rango de peso
    peso_min = django_filters.NumberFilter(field_name='peso', lookup_expr='gte')
    peso_max = django_filters.NumberFilter(field_name='peso', lookup_expr='lte')

    # Rango de año
    año_lanzamiento_min = django_filters.NumberFilter(field_name='año_lanzamiento', lookup_expr='gte')
    año_lanzamiento_max = django_filters.NumberFilter(field_name='año_lanzamiento', lookup_expr='lte')

    # Rango de reseñas (puntuación promedio)
    resenas_min = django_filters.NumberFilter(field_name='resenas', lookup_expr='gte')
    resenas_max = django_filters.NumberFilter(field_name='resenas', lookup_expr='lte')

    # Tecnologías (contiene una o más palabras)
    tecnologias = django_filters.CharFilter(method='filter_tecnologias', label='Tecnologías (contiene)')

    def filter_tecnologias(self, queryset, name, value):
        return queryset.filter(tecnologias__icontains=value)

    class Meta:
        model = Pala
        fields = [
            'nombre',
            'marca',
            'tienda',
            'forma',
            'nivel',
            'material_marco',
            'material_caras',
            'goma_nucleo',
            'balance',
            'genero',
        ]
