import pandas as pd

# 1. TUS DATOS (Los mismos de antes)
candidatos = [
    {"nombre": "Lautaro", "goles": 21, "partidos": 38},
    {"nombre": "Kane", "goles": 30, "partidos": 38},
    {"nombre": "Isak", "goles": 10, "partidos": 32},
    {"nombre": "Osimhen", "goles": 26, "partidos": 32}
]

# 2. CREAR DATAFRAME Y CALCULAR
tabla = pd.DataFrame(candidatos)
tabla["promedio"] = tabla["goles"] / tabla["partidos"]

# 3. FILTRAR (Solo los cracks)
cracks = tabla[tabla["promedio"] >= 0.5]

# --- AQUI ESTA LA NOVEDAD: EXPORTAR ---

# Usamos el método .to_csv()
# Parametro 1: El nombre del archivo que quieres crear.
# Parametro 2 (index=False): Importante para que no guarde los números 0,1,2 de la izquierda.
print("Guardando archivo...")
cracks.to_csv("Informe_Fichajes.csv", index=False)

print("¡Archivo 'Informe_Fichajes.csv' creado con éxito!")
