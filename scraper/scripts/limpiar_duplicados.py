import pandas as pd
import unidecode
import re

# Cargar el CSV combinado
df = pd.read_csv('../data/processed/precios_palas_combinadas.csv')

# Paso 1: Normalizar nombres
def normalizar_nombre(nombre):
    nombre = nombre.lower()
    nombre = unidecode.unidecode(nombre)  # quitar acentos
    nombre = re.sub(r'[^a-z0-9]', '', nombre)  # quitar todo menos letras y números
    return nombre

df['nombre_normalizado'] = df['nombre'].apply(normalizar_nombre)

# Paso 2: Duplicados potenciales entre distintas tiendas
duplicados_por_modelo = df.groupby('nombre_normalizado')['tienda'].nunique()
duplicados_multi_tienda = duplicados_por_modelo[duplicados_por_modelo > 1]

print(f"Hay {len(duplicados_multi_tienda)} palas vendidas en más de una tienda.\n")
print(df[df['nombre_normalizado'].isin(duplicados_multi_tienda.index)].sort_values('nombre_normalizado'))

# Paso 3: Detectar y limpiar duplicados dentro de la MISMA tienda
duplicados_misma_tienda = df.duplicated(subset=['nombre_normalizado', 'tienda'], keep=False)

df_duplicados_misma_tienda = df[duplicados_misma_tienda].sort_values(['nombre_normalizado', 'tienda'])

# Mostrar duplicados internos
print("\nDuplicados dentro de la misma tienda:")
print(df_duplicados_misma_tienda)

# Opcional: limpiar duplicados dejando solo el más barato
df_sin_duplicados = df.sort_values('precio').drop_duplicates(subset=['nombre_normalizado', 'tienda'], keep='first')

# Guardar resultado limpio si quieres
df_sin_duplicados.drop(columns='nombre_normalizado').to_csv('../data/processed/palas_sin_duplicados.csv', index=False)
