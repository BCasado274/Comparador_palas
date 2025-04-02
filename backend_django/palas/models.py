from django.db import models

class Pala(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField()
    url = models.URLField()
    imagen = models.URLField()
    tienda = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.tienda}"
