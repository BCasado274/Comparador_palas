##(el root de tu proyecto)
##Este archivo delega rutas a la app palas

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/palas/', include('palas.urls')),  # ✅ Enlaza con las URLs de la app
]

