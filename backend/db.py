import sqlite3
import os

# Ruta relativa desde backend/ hasta db/palas.db
DB_PATH = os.path.join('..', 'db', 'palas.db')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # para obtener diccionarios en lugar de tuplas
    return conn
