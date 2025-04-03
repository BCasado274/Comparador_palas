import pandas as pd
from duckduckgo_search import DDGS
import time

ruta_csv = '../data/processed/palas_sin_duplicados.csv'
df = pd.read_csv(ruta_csv)
nombres_palas = df['nombre'].drop_duplicates().tolist()

def buscar_url_pala(nombre_pala):
    query = f"{nombre_pala} ficha técnica site:padelnuestro.com OR site:padeliberico.es"
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=1)
            for r in results:
                url = r.get('href')
                # Solo aceptamos si es padelnuestro o padeliberico
                if url and ('padelnuestro.com' in url or 'padeliberico.es' in url):
                    return url
    except Exception as e:
        print(f"⚠️ Error con '{nombre_pala}': {e}")
    return None

resultados = []

for i, nombre in enumerate(nombres_palas[:15]):  # Solo 15 para asegurar que algunos funcionen
    url = buscar_url_pala(nombre)
    if url:
        resultados.append({'nombre': nombre, 'url': url})
        print(f"{i+1:02d} ✅ {nombre} → {url}")
    else:
        print(f"{i+1:02d} ❌ {nombre} → No encontrada")
    time.sleep(2.5)

# Guardar archivo reducido
df_urls = pd.DataFrame(resultados)
df_urls.to_csv('../data/processed/urls_detectadas.csv', index=False)
print("\n✅ URLs guardadas en ../data/processed/urls_detectadas.csv")
