import sqlite3
import pandas as pd
import os

# Ruta al CSV limpio
csv_path = os.path.join('..', 'data', 'processed', 'palas_sin_duplicados.csv')

# Ruta a la base de datos
db_path = os.path.join('..', '..', 'db', 'palas.db')

# Conectar (crea la base si no existe)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS palas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    url TEXT,
    imagen TEXT,
    tienda TEXT NOT NULL
)
''')

# Leer el CSV
df = pd.read_csv(csv_path)

# Limpiar tabla (opcional: si quieres reiniciar antes de insertar)
cursor.execute('DELETE FROM palas')

# Insertar cada fila
for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO palas (nombre, precio, url, imagen, tienda)
        VALUES (?, ?, ?, ?, ?)
    ''', (row['nombre'], row['precio'], row['url'], row['imagen'], row['tienda']))

# Confirmar y cerrar
conn.commit()
conn.close()

print("✅ Datos insertados correctamente en la base de datos.")
