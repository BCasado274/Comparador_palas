import pandas as pd
from duckduckgo_search import DDGS
import time

# Ruta al CSV con las palas
ruta_csv = '../data/processed/palas_sin_duplicados.csv'

# Cargar el archivo y extraer nombres únicos
df = pd.read_csv(ruta_csv)
nombres_palas = df['nombre'].drop_duplicates().tolist()

print(f"🔍 Se encontraron {len(nombres_palas)} palas únicas.")

# Buscar URLs en padelnuestro y padeliberico
def buscar_url_pala(nombre_pala):
    query = f"{nombre_pala} ficha técnica site:padelnuestro.com OR site:padeliberico.es"
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=1)
            for r in results:
                return r.get('href')
    except Exception as e:
        print(f"⚠️ Error con '{nombre_pala}': {e}")
    return None

# Buscar y guardar resultados
resultados = []

for i, nombre in enumerate(nombres_palas):
    url = buscar_url_pala(nombre)
    resultados.append({'nombre': nombre, 'url': url})
    print(f"{i+1:03d}/{len(nombres_palas)} - {nombre} → {url if url else '❌ No encontrada'}")
    time.sleep(7)  # Pausa para evitar bloqueo

# Guardar en CSV
output_csv = '../data/processed/urls_detectadas.csv'
pd.DataFrame(resultados).to_csv(output_csv, index=False)
print(f"\n✅ URLs guardadas en: {output_csv}")
