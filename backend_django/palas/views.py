from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pala
from .serializers import PalaSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import PalaFilter

# @api_view(['GET'])
# def listar_palas(request):
#     palas = Pala.objects.all()
#     serializer = PalaSerializer(palas, many=True)
#     return Response(serializer.data)

# Create your views here.

class PalaListAPIView(generics.ListAPIView):
    queryset = Pala.objects.all()
    serializer_class = PalaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PalaFilter
    search_fields = ['nombre']
    ordering_fields = ['precio']

def get_distinct_values(field_name):
    return Pala.objects.exclude(**{f"{field_name}__isnull": True}).exclude(**{field_name: ""})\
               .values_list(field_name, flat=True).distinct().order_by(field_name)

@api_view(['GET'])
def listar_marcas(request):
    marcas = Pala.objects.values_list('marca', flat=True).distinct().order_by('marca')
    return Response(marcas)
    
@api_view(['GET'])
def listar_tiendas(request):
    return Response(get_distinct_values('tienda'))

@api_view(['GET'])
def listar_formas(request):
    return Response(get_distinct_values('forma'))

@api_view(['GET'])
def listar_niveles(request):
    return Response(get_distinct_values('nivel'))

@api_view(['GET'])
def listar_materiales_marco(request):
    return Response(get_distinct_values('material_marco'))

@api_view(['GET'])
def listar_materiales_caras(request):
    return Response(get_distinct_values('material_caras'))

@api_view(['GET'])
def listar_gomas(request):
    return Response(get_distinct_values('goma_nucleo'))

@api_view(['GET'])
def listar_balances(request):
    return Response(get_distinct_values('balance'))

@api_view(['GET'])
def listar_generos(request):
    return Response(get_distinct_values('genero'))

@api_view(['GET'])
def listar_tecnologias(request):
    # Extrae todas las tecnologías separadas por coma y las unifica
    tecnologias_raw = Pala.objects.exclude(tecnologias__isnull=True).exclude(tecnologias='')\
                        .values_list('tecnologias', flat=True)

    tecnologias_unicas = set()
    for tech_list in tecnologias_raw:
        partes = [t.strip() for t in tech_list.split(',')]
        tecnologias_unicas.update(partes)

    return Response(sorted(tecnologias_unicas))