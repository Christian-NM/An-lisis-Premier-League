# 1. LISTAS (LIST):
# Creamos la lista 'jugadores' con 4 elementos de texto (Strings).
jugadores = ["Mbappé", "Haaland", "Militao", "Vitinha"]

# 2. MÉTODOS DE LISTA (.remove):
# Buscamos exactamente el valor "Militao" y lo borramos.
# La lista ahora se queda con 3 elementos. Los índices se reorganizan automáticamente.
jugadores.remove("Militao")

# 3. IMPRIMIR LISTA ENTERA:
# Vemos cómo ha quedado la lista tras el borrado: ['Mbappé', 'Haaland', 'Vitinha']
print(jugadores)

# 4. ÍNDICES NEGATIVOS:
# [-1] es un truco de Python para pedir "el último elemento", sin importar lo larga que sea la lista.
# En este caso, imprimirá "Vitinha".
print(jugadores[-1])

# 5. BUCLE FOR (Iteración):
# "Por cada 'jugador' (variable temporal) que encuentres en la lista 'jugadores'..."
for jugador in jugadores:
    # Esta línea tiene sangría (espacios), así que se repite 3 veces (una por nombre).
    print(f"Analizando estadísticas de: {jugador}")

    # ¡OJO AQUÍ!
    # Esta línea TAMBIÉN tiene sangría. Por tanto, está DENTRO del bucle.
    # Se imprimirá 3 veces, justo después de cada nombre.
    # Si quisieras que saliera solo una vez al final, deberías quitarle los espacios del principio.
    print("Fin del informe.")

    # 6. DICCIONARIO (DICT):
# Usamos llaves {} para crear una estructura de Clave: Valor.
# Es como una ficha de papel donde etiquetas cada dato.
Haaland = {
    "nombre": "Erling Haaland",     # Clave "nombre" -> Valor Texto
    "equipo": "Manchester City",    # Clave "equipo" -> Valor Texto
    "goles": 27,                    # Clave "goles"  -> Valor Entero (Int)
}
# Ahora la variable 'Haaland' contiene toda esa información junta.

# 7. LISTA DE DICCIONARIOS:
# Creamos una lista [] que contiene tres diccionarios {} dentro.
# Esto es exactamente lo que te devuelve una API de fútbol cuando pides "Goleadores de la Premier".
equipo = [
    {"nombre": "Haaland", "goles": 27},
    {"nombre": "De Bruyne", "goles": 4},
    {"nombre": "Rodri", "goles": 2}
]

# 8. BUCLE SOBRE DATOS COMPLEJOS:
# En cada vuelta, la variable 'jugador' NO es solo un nombre, es el DICCIONARIO COMPLETO de esa persona.
# Vuelta 1: jugador = {"nombre": "Haaland", "goles": 27}
for jugador in equipo:

    # 9. EXTRACCIÓN DE DATOS:
    # Accedemos a los datos internos usando la CLAVE entre corchetes y comillas.
    # Sacamos el valor de "nombre" y lo guardamos en una variable auxiliar 'nombre'.
    nombre = jugador["nombre"]
    # Sacamos el valor de "goles" y lo guardamos en 'goles'.
    goles = jugador["goles"]

    # 10. USO DE DATOS EXTRAÍDOS:
    # Usamos el f-string para mostrar los datos limpios que acabamos de sacar.
    print(f"{nombre} lleva {goles} goles.")

# 11. FIN DEL PROCESO:
# Esta línea NO tiene sangría (está pegada a la izquierda).
# Por tanto, está FUERA del bucle y solo se ejecuta una vez, cuando la lista se ha terminado.
print("Análisis del equipo finalizado.")
