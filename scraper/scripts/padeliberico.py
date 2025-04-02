import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://www.padeliberico.es/palas-de-padel"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}
OUTPUT_FILE = "palas_padeliberico.csv"

def extraer_productos(pagina):
    url = f"{BASE_URL}?page={pagina}"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.select(".product-miniature")

    productos = []
    for item in items:
        nombre_tag = item.select_one(".product-title a")
        precio_tag = item.select_one(".price")
        imagen_tag = item.select_one("img")

        if nombre_tag and precio_tag and imagen_tag:
            productos.append({
                "nombre": nombre_tag.text.strip(),
                "precio": precio_tag.text.strip(),
                "url": nombre_tag["href"].strip(),
                "imagen": imagen_tag["src"].strip(),
                "tienda": "Pádel Ibérico"
            })

    print(f"📄 Página {pagina}: {len(productos)} productos")
    return productos

def scrapear_todas(max_paginas=30):
    todos = []
    for pagina in range(1, max_paginas + 1):
        productos = extraer_productos(pagina)
        if not productos:
            break
        todos.extend(productos)
        time.sleep(1)  # 👈 Pausa entre peticiones para no saturar

    return todos

def guardar_csv(productos):
    campos = ["nombre", "precio", "url", "imagen", "tienda"]
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(productos)
    print(f"\n✅ Archivo '{OUTPUT_FILE}' guardado con {len(productos)} productos.")

if __name__ == "__main__":
    productos = scrapear_todas()
    guardar_csv(productos)
