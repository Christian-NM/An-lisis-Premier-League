import pandas as pd
import requests
import matplotlib.pyplot as plt
from io import StringIO

# --- 1. EXTRACCIÓN (Scraping) ---
print("1. Conectando con Wikipedia...")

url = "https://en.wikipedia.org/wiki/2023%E2%80%9324_Premier_League"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

respuesta = requests.get(url, headers=headers)
tablas = pd.read_html(StringIO(respuesta.text))

# Buscamos la tabla de clasificación
clasificacion = tablas[4]

# --- 2. LIMPIEZA (Cleaning) ---
print("2. Limpiando datos...")

# Renombramos columnas
clasificacion = clasificacion.rename(
    columns={"Team": "Equipo", "Pts": "Puntos"})

# --- ¡LA CORRECCIÓN ESTÁ AQUÍ! ---
# Convertimos la columna "Puntos" a números reales.
# errors='coerce' significa: "Si encuentras algo que no sea número, bórralo, pero no me des error".
clasificacion["Puntos"] = pd.to_numeric(
    clasificacion["Puntos"], errors='coerce')

# Nos quedamos con el Top 5
top_5 = clasificacion.head(5)

print("\n--- TOP 5 PREMIER LEAGUE ---")
print(top_5[["Equipo", "Puntos"]])

# --- 3. VISUALIZACIÓN (Matplotlib) ---
print("3. Generando gráfico...")

plt.figure(figsize=(10, 6))

# Gráfico de barras
plt.bar(top_5["Equipo"], top_5["Puntos"], color="skyblue")

plt.title("Premier League 23/24 - Top 5 Equipos")
plt.xlabel("Clubes")
plt.ylabel("Puntos")

# Añadimos los números encima de las barras
for i in range(len(top_5)):
    # Ahora sí podemos sumar +1 porque "Puntos" ya es un número
    plt.text(i, top_5["Puntos"][i] + 1, int(top_5["Puntos"][i]), ha='center')

plt.show()
