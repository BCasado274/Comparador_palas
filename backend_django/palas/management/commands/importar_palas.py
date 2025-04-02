import csv
import os
from django.core.management.base import BaseCommand
from palas.models import Pala

# Diccionario de sinónimos → marca oficial
MARCAS_EQUIVALENTES = {
    'adidas': 'Adidas',
    'akkeron': 'Akkeron',
    'babolat': 'Babolat',
    'beach': 'Beach',
    'beachtennis': 'Beachtennis',
    'black crown': 'Black Crown',
    'bullpadel': 'Bullpadel',
    'drop': 'Drop',
    'dunlop': 'Dunlop',
    'enebe': 'Enebe',
    'hbl': 'Hbl',
    'head': 'Head',
    'higer': 'Higer',
    'joma': 'Joma',
    'kelme': 'Kelme',
    'kombat': 'Kombat',
    'lok': 'Lok',
    'middle moon': 'Middle Moon',
    'mystica': 'Mystica',
    'nexus': 'Nexus',
    'nox': 'Nox',
    'orygen': 'Orygen',
    'pack': 'Pack',
    'pala': 'Pala',
    'pickleball': 'Pickleball',
    'prince': 'Prince',
    'royal': 'Royal',
    'rs': 'Rs',
    'salming': 'Salming',
    'siux': 'Siux',
    'softee': 'Softee',
    'star': 'Star',
    'starvie': 'Starvie',
    'tecnifibre': 'Tecnifibre',
    'vairo': 'Vairo',
    'varlion': 'Varlion',
    'vibor-a': 'Vibor-a',
    'vibora': 'Vibor-a',
    'víbora': 'Vibor-a',
    'wilson': 'Wilson',
    'wingpadel': 'Wingpadel'
}

def detectar_marca(nombre_pala):
    nombre_lower = nombre_pala.lower()
    for marca in MARCAS_EQUIVALENTES:
        if marca.lower() in nombre_lower:
            return marca
    return "Desconocida"

class Command(BaseCommand):
    help = 'Importa palas desde el archivo CSV limpio'

    def handle(self, *args, **kwargs):
        # Ruta al CSV relativo al manage.py
        ruta_csv = os.path.join('..', 'scraper', 'data', 'processed', 'palas_sin_duplicados.csv')

        if not os.path.exists(ruta_csv):
            self.stderr.write(f"❌ No se encontró el archivo: {ruta_csv}")
            return

        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            total = 0
            for row in reader:
                try:
                    nombre = row['nombre']
                    marca = detectar_marca(nombre)
                    precio = float(str(row['precio']).replace(',', '.').replace('€', '').strip())
                    
                    Pala.objects.create(
                        nombre=nombre,
                        marca=marca,
                        precio=precio,
                        url=row['url'],
                        imagen=row['imagen'],
                        tienda=row['tienda']
                    )
                    total += 1
                except Exception as e:
                    self.stderr.write(f"⚠️ Error con la fila: {row['nombre']} - {e}")

        self.stdout.write(self.style.SUCCESS(f"✅ Se importaron {total} palas correctamente."))
