import requests
from bs4 import BeautifulSoup

print("--- INICIANDO OPERACIÓN SCRAPING ---")

# 1. OBJETIVO
url = "http://quotes.toscrape.com/"

# 2. DESCARGAR LA WEB (Traer el código HTML a tu PC)
respuesta = requests.get(url)
print(f"Estado de la conexión: {respuesta.status_code}")

# 3. COCINAR LA SOPA (Parsear)
# BeautifulSoup convierte ese texto HTML feo en un objeto ordenado
sopa = BeautifulSoup(respuesta.text, "html.parser")

# 4. BUSCAR EL TESORO
# En HTML, los títulos suelen estar en etiquetas <h1> o <h2>
# y las frases en esta web están en etiquetas <span> con clase "text"

# Le decimos: "Búscame todos los <span> que tengan la clase 'text'"
frases = sopa.find_all("span", class_="text")

print(f"\n¡He encontrado {len(frases)} frases!\n")

# 5. MOSTRAR EL BOTÍN
# Recorremos la lista de resultados (¡Bucle for otra vez!)
for frase in frases:
    # .text elimina las etiquetas <span> y deja solo la frase limpia
    print(frase.text)
    print("---")
