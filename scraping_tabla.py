import pandas as pd
import requests
from io import StringIO  # Herramienta necesaria para pasar el texto a Pandas

print("--- DESCARGANDO DATOS DE WIKIPEDIA (MODO SIGILOSO) ---")

url = "https://en.wikipedia.org/wiki/2023%E2%80%9324_Premier_League"

# 1. EL DISFRAZ (Headers)
# Le decimos: "Hola, soy un navegador Mozilla/Chrome en Windows", no soy un robot.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# 2. HACER LA PETICIÓN CON EL DISFRAZ
# Usamos requests primero porque nos deja añadir los headers (pd.read_html a secas no deja)
respuesta = requests.get(url, headers=headers)

# Verificamos si nos dejó entrar (200 = OK)
print(f"Código de respuesta: {respuesta.status_code}")

if respuesta.status_code == 200:
    # 3. LEER EL HTML
    # Pasamos el TEXTO de la respuesta a Pandas.
    # Usamos StringIO para que Pandas lo trate como un archivo en memoria.
    tablas = pd.read_html(StringIO(respuesta.text))

    print(f"¡He encontrado {len(tablas)} tablas!")

    # 4. BUSCAR LA TABLA CORRECTA
    # En Wikipedia las tablas cambian de sitio. Vamos a buscar la clasificación.
    # Suele ser la tabla número 4 o 5 (índice 4).
    clasificacion = tablas[4]

    print("\n--- VISTA PREVIA ---")
    print(clasificacion.head(5))

    # 5. GUARDAR
    clasificacion.to_csv("Premier_23_24.csv", index=False)
    print("\n¡Archivo guardado con éxito!")

else:
    print("El portero nos ha pillado. Intenta cambiar el User-Agent.")
