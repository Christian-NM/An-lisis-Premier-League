
# VECTORIZACION DE OPERACIONES CON PANDAS

import pandas as pd


candidatos = [
    {"Nombre": "Lautaro", "Goles": 21, "Partidos": 38},
    {"Nombre": "Kane", "Goles": 30, "Partidos": 38},
    {"Nombre": "Isak", "Goles": 10, "Partidos": 32},
    {"Nombre": "Osimhen", "Goles": 26, "Partidos": 32}
]

tabla = pd.DataFrame(candidatos)

print("--- INFORME DE SCOUTING ---")

# --- AQUI ESTA LA MAGIA ---
# Le decimos: "Crea una columna nueva llamada 'promedio'..."
# "...y rellénala dividiendo TODA la columna 'Goles' entre TODA la columna 'Partidos' a la vez"
tabla["Promedio"] = tabla["Goles"] / tabla["Partidos"]

# Imprimimos para ver la nueva columna
print(tabla)
