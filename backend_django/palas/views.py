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


@api_view(['GET'])
def listar_marcas(request):
    marcas = Pala.objects.values_list('marca', flat=True).distinct().order_by('marca')
    return Response(marcas)
    