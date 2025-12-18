import requests
import pandas as pd

print("--- LLAMANDO A LA API DE PRUEBA ---")

# 1. URL NUEVA (Esta es una API de pruebas de Google/Typicode que nunca falla)
# Nos devuelve una lista de 10 usuarios falsos con sus datos.
url = "https://jsonplaceholder.typicode.com/users"

# 2. PETICIÓN
respuesta = requests.get(url)

print(f"Código de estado: {respuesta.status_code}")  # Debería salir 200

if respuesta.status_code == 200:
    print("¡Conexión exitosa! El camarero trae los datos 🥘")

    # 3. CONVERTIR A PYTHON
    datos = respuesta.json()

    # 4. CREAR TABLA
    # Como la estructura es una lista de diccionarios (igual que tus jugadores),
    # Pandas lo entiende perfectamente.
    tabla = pd.DataFrame(datos)

    # 5. LIMPIEZA RÁPIDA
    # Vamos a quedarnos solo con columnas que nos interesen para que se vea bien
    tabla_limpia = tabla[["id", "name", "email", "website"]]

    print("\n--- BASE DE DATOS RECIBIDA ---")
    print(tabla_limpia)

    # EXTRA: ¡Guardémoslo para demostrar que funciona!
    tabla_limpia.to_csv("Usuarios_API.csv", index=False)
    print("\n¡Archivo 'Usuarios_API.csv' guardado en tu carpeta!")

else:
    print("Error 404: La URL sigue mal.")
