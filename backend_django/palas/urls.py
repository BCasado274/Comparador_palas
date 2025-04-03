# palas/urls.py
#las URLs de la app

from django.urls import path
from .views import (
    PalaListAPIView,
    listar_marcas, listar_tiendas, listar_formas, listar_niveles,
    listar_materiales_marco, listar_materiales_caras, listar_gomas,
    listar_balances, listar_generos, listar_tecnologias
)


urlpatterns = [
    path('', PalaListAPIView.as_view(), name='pala-list'),
    path('marcas/', listar_marcas),
    path('tiendas/', listar_tiendas),
    path('formas/', listar_formas),
    path('niveles/', listar_niveles),
    path('materiales-marco/', listar_materiales_marco),
    path('materiales-caras/', listar_materiales_caras),
    path('gomas/', listar_gomas),
    path('balances/', listar_balances),
    path('generos/', listar_generos),
    path('tecnologias/', listar_tecnologias),
]