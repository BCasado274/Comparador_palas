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
    for clave, marca_oficial in MARCAS_EQUIVALENTES.items():
        if clave in nombre_lower:
            return marca_oficial
    return "Desconocida"

# ✅ Nuevo: cargar detalles técnicos desde CSV
DETALLES_TECNICOS_PATH = os.path.join('..', 'scraper', 'data', 'processed', 'detalles_tecnicos.csv')

def cargar_detalles_tecnicos():
    detalles = {}
    if os.path.exists(DETALLES_TECNICOS_PATH):
        with open(DETALLES_TECNICOS_PATH, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                nombre = row['nombre'].strip().lower()
                detalles[nombre] = row
    return detalles

class Command(BaseCommand):
    help = 'Importa palas desde el archivo CSV limpio y enriquece con detalles técnicos'

    def handle(self, *args, **kwargs):
        ruta_csv = os.path.join('..', 'scraper', 'data', 'processed', 'palas_sin_duplicados.csv')
        detalles_tecnicos = cargar_detalles_tecnicos()

        if not os.path.exists(ruta_csv):
            self.stderr.write(f"❌ No se encontró el archivo: {ruta_csv}")
            return

        with open(ruta_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            total = 0
            for row in reader:
                try:
                    nombre = row['nombre']
                    clave = nombre.strip().lower()
                    detalles = detalles_tecnicos.get(clave, {})

                    Pala.objects.create(
                        nombre=nombre,
                        marca=detectar_marca(nombre),
                        precio=float(str(row['precio']).replace(',', '.').replace('€', '').strip()),
                        url=row['url'],
                        imagen=row['imagen'],
                        tienda=row['tienda'],

                        # Campos técnicos adicionales
                        forma=detalles.get('forma'),
                        peso=int(detalles['peso']) if detalles.get('peso') else None,
                        nivel=detalles.get('nivel'),
                        material_marco=detalles.get('material_marco'),
                        material_caras=detalles.get('material_caras'),
                        goma_nucleo=detalles.get('goma_nucleo'),
                        balance=detalles.get('balance'),
                        tecnologias=detalles.get('tecnologias'),
                        genero=detalles.get('genero'),
                        año_lanzamiento=int(detalles['año_lanzamiento']) if detalles.get('año_lanzamiento') else None,
                        resenas=float(detalles['resenas']) if detalles.get('resenas') else None
                    )
                    total += 1
                except Exception as e:
                    self.stderr.write(f"⚠️ Error con la fila: {row['nombre']} - {e}")

        self.stdout.write(self.style.SUCCESS(f"✅ Se importaron {total} palas correctamente."))
