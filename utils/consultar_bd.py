import sqlite3
import os

# Ruta a la base de datos
db_path = os.path.join('..', '..', 'db', 'palas.db')

# Conectar
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Consultar las primeras 10 palas
cursor.execute("SELECT nombre, precio, tienda FROM palas LIMIT 10")
resultados = cursor.fetchall()

print("🔍 Palas en la base de datos:\n")
for nombre, precio, tienda in resultados:
    print(f"🏓 {nombre} | 💰 {precio} € | 🏪 {tienda}")

conn.close()
