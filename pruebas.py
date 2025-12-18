# Imaginemos que acabamos de descargar esto de una API de fútbol profesional
# Fíjate que hay diccionarios {} DENTRO de otros diccionarios {}
respuesta_partido = {
    "id_partido": 85430,
    "competicion": "Champions League",
    "estadio": "Santiago Bernabéu",
    "resultado": {
        "local": 2,  # Real Madrid
        "visitante": 1  # Bayern
    },
    "goleadores": [
        {"nombre": "Vinicius", "minuto": 25},
        {"nombre": "Davies", "minuto": 68},
        {"nombre": "Joselu", "minuto": 88}
    ]
}

print("--- ANALIZANDO RESPUESTA DE LA API ---")

# EJEMPLO 1: Sacar un dato fácil (Nivel 1)
torneo = respuesta_partido["competicion"]
print(f"Torneo: {torneo}")

# EJEMPLO 2: Sacar un dato anidado (Nivel 2)
# Para llegar a los goles del local, entramos en 'resultado' Y LUEGO en 'local'
goles_rm = respuesta_partido["resultado"]["local"]
print(f"Goles del Local: {goles_rm}")

# --- AHORA TÚ ---

# RETO 1: Imprime el nombre del estadio.
estadio = respuesta_partido["estadio"]
print(f"Jugado en: {estadio}")

# RETO 2 (DIFÍCIL): Imprime el nombre del jugador que marcó el ÚLTIMO gol.
# Pista: 'goleadores' es una LISTA. El último es el índice [-1].
# Y dentro de ese, quieres el campo "nombre".
heroe = respuesta_partido["goleadores"][-1]["nombre"]

print(f"El héroe del partido fue: {heroe}")
