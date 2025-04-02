from django.db import models

class Pala(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    url = models.URLField()
    imagen = models.URLField()
    tienda = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)


    #Campos técnicos
    forma = models.CharField(max_length=50, blank=True, null=True)
    peso = models.IntegerField(blank=True, null=True)  # en gramos
    nivel = models.CharField(max_length=50, blank=True, null=True)
    material_marco = models.CharField(max_length=100, blank=True, null=True)
    material_caras = models.CharField(max_length=100, blank=True, null=True)
    goma_nucleo = models.CharField(max_length=50, blank=True, null=True)
    balance = models.CharField(max_length=50, blank=True, null=True)
    tecnologias = models.TextField(blank=True, null=True)  # separadas por coma
    genero = models.CharField(max_length=20, blank=True, null=True)
    año_lanzamiento = models.IntegerField(blank=True, null=True)
    resenas = models.FloatField(blank=True, null=True)  # puntuación promedio

    def __str__(self):
        return f"{self.nombre} - {self.tienda}"
