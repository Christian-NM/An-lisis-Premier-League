
import pandas as pd

print("--- Cargando base de datos del Scouting ---")

# 1. LEER EL ARCHIVO
# La función read_csv busca el archivo en tu carpeta y lo convierte en DataFrame
# IMPORTANTE: El nombre debe ser EXACTO (incluyendo .csv)
df = pd.read_csv("Informe_Fichajes.csv")

# 2. VERIFICAR QUE SE HA CARGADO
print("¡Archivo cargado correctamente!")
print(df)
# ... (código anterior) ...

print("\n--- 1. LOS PRIMEROS (head) ---")
# .head(n) te enseña solo las primeras 'n' filas. Ideal para ver qué pinta tiene.
print(df.head(2))

print("\n--- 2. INFORMACIÓN TÉCNICA (info) ---")
# .info() te dice si hay huecos vacíos (nulos) y de qué tipo son los datos (enteros, texto...)
# Vital para el punto "Limpieza de datos" de tu guía.
print(df.info())

print("\n--- 3. ESTADÍSTICAS RÁPIDAS (describe) ---")
# .describe() calcula la media, el máximo, el mínimo... de todas las columnas numéricas AUTOMÁTICAMENTE.
print(df.describe())
