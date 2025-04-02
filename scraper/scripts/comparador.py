import csv

def leer_csv(nombre_archivo, tienda):
    productos = []
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["tienda"] = tienda
            productos.append(row)
    return productos

def guardar_csv_combinado(productos, archivo_salida="../data/processed/precios_palas_combinadas.csv"):
    campos = ["nombre", "precio", "url", "imagen", "tienda"]
    with open(archivo_salida, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(productos)

def main():
    productos_padelnuestro = leer_csv("../data/raw/palas_padelnuestro.csv", "PadelNuestro")
    productos_streetpadel = leer_csv("../data/raw/palas_padeliberico.csv", "PadelIberico")

    todos = productos_padelnuestro + productos_streetpadel
    print(f"📦 Total productos combinados: {len(todos)}")

    guardar_csv_combinado(todos)
    print("✅ Archivo 'precios_palas_combinadas.csv' generado correctamente.")

if __name__ == "__main__":
    main()
