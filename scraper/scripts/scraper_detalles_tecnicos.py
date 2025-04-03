import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

# Cargar URLs detectadas
df_urls = pd.read_csv('../data/processed/urls_detectadas.csv')
resultados = []

def limpiar_texto(t):
    return t.replace('\xa0', ' ').strip() if t else ""

def scrapear_padelnuestro(url):
    try:
        r = requests.get(url, headers=headers)
        print(f"🔗 Accediendo a: {url}")
        print("📝 HTML recibido:")
        print(r.text[:2000])  # Mostramos solo los primeros 2000 caracteres para no saturar

        soup = BeautifulSoup(r.text, 'html.parser')

        datos = {
            'forma': None, 'peso': None, 'nivel': None, 'material_marco': None,
            'material_caras': None, 'goma_nucleo': None, 'balance': None,
            'tecnologias': [], 'genero': None, 'año_lanzamiento': None, 'resenas': None
        }

        # Buscar todos los bloques de características
        atributos = soup.find_all("div", class_="description-attributes")

        for attr in atributos:
            clave = attr.find("span", class_="description-attributes-label").get_text(strip=True).lower()
            valor = attr.find("span", class_="description-attributes-value").get_text(strip=True)

            if 'forma' in clave or 'formato' in clave:
                datos['forma'] = valor
            elif 'peso' in clave:
                datos['peso'] = valor
            elif 'nivel' in clave:
                datos['nivel'] = valor
            elif 'balance' in clave:
                datos['balance'] = valor
            elif 'núcleo' in clave or 'goma' in clave:
                datos['goma_nucleo'] = valor
            elif 'cara' in clave:
                datos['material_caras'] = valor
            elif 'marco' in clave:
                datos['material_marco'] = valor
            elif 'sexo' in clave or 'género' in clave or 'jugador' in clave:
                datos['genero'] = valor
            elif 'año' in clave:
                datos['año_lanzamiento'] = valor
            elif 'acabado' in clave or 'tecnolog' in clave or 'superficie' in clave:
                datos['tecnologias'].append(valor)

        # Unir las tecnologías en una cadena separada por comas
        datos['tecnologias'] = ', '.join(datos['tecnologias'])

        return datos

    except Exception as e:
        print(f"⚠️ Error en {url} → {e}")
        return {}

def scrapear_padeliberico(url):
    # Podés añadir scraping específico para padeliberico.es aquí cuando estés listo
    return {}

# Recorrer cada URL
for _, row in df_urls.iterrows():
    nombre = row['nombre']
    url = row['url']
    print(f"🔎 Procesando: {nombre}")

    if 'padelnuestro.com' in url:
        datos = scrapear_padelnuestro(url)
    elif 'padeliberico.es' in url:
        datos = scrapear_padeliberico(url)
    else:
        print(f"❌ URL desconocida: {url}")
        continue

    resultados.append({
        'nombre': nombre,
        **datos
    })

# Guardar resultados
df_resultado = pd.DataFrame(resultados)
df_resultado.to_csv('../data/processed/detalles_tecnicos2.csv', index=False)
print("✅ Archivo generado: detalles_tecnicos2.csv")
