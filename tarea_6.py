# --- PASO 1: LA HERRAMIENTA ---
# Define la función 'calcular_promedio' que acepte (goles, partidos)
# y devuelva (return) el resultado de la división.
def calcular_promedio(goles, partidos):
    resultado = goles / partidos
    return resultado


# --- PASO 2: LOS DATOS (Esto te lo doy yo) ---
candidatos = [
    {"nombre": "Lautaro", "goles": 21, "partidos": 38},
    {"nombre": "Kane", "goles": 30, "partidos": 38},
    {"nombre": "Isak", "goles": 10, "partidos": 32},
    {"nombre": "Osimhen", "goles": 26, "partidos": 32}
]

print("--- INFORME DE SCOUTING ---")

# --- PASO 3: EL PROCESO ---
# Crea un bucle que recorra la lista 'candidatos'
for jugador in candidatos:

    # A. Extrae los datos necesarios del diccionario
    nombre = jugador["nombre"]
    goles = jugador["goles"]
    partidos = jugador["partidos"]

    # B. Usa TU función del PASO 1 para calcular la media de ESTE jugador
    media = calcular_promedio(goles, partidos)

    # C. Aplica la LÓGICA (if/else)
    # Si la media es mayor o igual (>=) a 0.5...
    if media >= 0.5:
        # Imprime "FICHAJE PRIORITARIO" y el nombre
        print(f"FICHAJE PRIORITARIO: {nombre} (Promedio: {media:.2f})")

    else:
        # Si no, imprime "DESCARTAR"
        print(f"DESCARTAR: {nombre} (Promedio: {media:.2f})")
print("--- Fin del reporte ---")
