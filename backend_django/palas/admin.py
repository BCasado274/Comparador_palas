from django.contrib import admin
from .models import Pala

@admin.register(Pala)
class PalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'tienda', 'marca')  # columnas visibles
    search_fields = ('nombre', 'tienda','marca')          # barra de búsqueda
    list_filter = ('tienda', 'marca')                     # filtro lateral

# Register your models here.
