# palas/urls.py
#las URLs de la app

from django.urls import path
from .views import PalaListAPIView, listar_marcas


urlpatterns = [
    path('', PalaListAPIView.as_view(), name='pala-list'),
    path('marcas/', listar_marcas, name='listar-marcas'),
]