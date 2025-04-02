import requests
from bs4 import BeautifulSoup
import csv
import math

BASE_URL = "https://www.padelnuestro.com"
CATEGORY_PATH = "/palas-padel"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def calcular_paginas_totales():
    url = f"{BASE_URL}{CATEGORY_PATH}"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    count_text = soup.select_one(".toolbar-amount")
    if count_text:
        text = count_text.text.strip()
        print("🧪 Palas encontradas:", text)

        try:
            total_products = int(text.split()[0])
            return math.ceil(total_products / 24)
        except ValueError:
            print("❌ No se pudo convertir a entero:", text.split()[0])

    print("❌ No se encontró el selector o el número total.")
    return 1

def extraer_productos_pagina(numero_pagina):
    url = f"{BASE_URL}{CATEGORY_PATH}?p={numero_pagina}"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.select(".product-item-info")
    print(f"📄 Página {numero_pagina} - Productos encontrados: {len(items)}")

    productos = []
    for item in items:
        name = item.select_one(".product-item-name a")
        price = item.select_one(".price")
        image = item.select_one("img")

        if name and price and image:
            productos.append({
                "nombre": name.text.strip(),
                "precio": price.text.strip(),
                "url": BASE_URL + name['href'],
                "imagen": image['src']
            })

    return productos

def guardar_en_csv(productos, nombre_archivo="palas_padelnuestro.csv"):
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["nombre", "precio", "url", "imagen"])
        writer.writeheader()
        writer.writerows(productos)

def ejecutar_scraper():
    total_paginas = calcular_paginas_totales()
    print(f"🔍 Se detectaron {total_paginas} páginas en total.")

    todos_los_productos = []

    for pagina in range(1, total_paginas + 1):
        productos = extraer_productos_pagina(pagina)
        todos_los_productos.extend(productos)

    print(f"\n✅ Se han extraído {len(todos_los_productos)} productos en total.")
    guardar_en_csv(todos_los_productos)

if __name__ == "__main__":
    ejecutar_scraper()
