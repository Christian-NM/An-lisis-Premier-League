import pandas as pd
import matplotlib.pyplot as plt

# 1. TUS DATOS
candidatos = [
    {"Nombre": "Lautaro", "Goles": 21, "Partidos": 38},
    {"Nombre": "Kane", "Goles": 30, "Partidos": 38},
    {"Nombre": "Isak", "Goles": 10, "Partidos": 32},
    {"Nombre": "Osimhen", "Goles": 26, "Partidos": 32}
]
tabla = pd.DataFrame(candidatos)

# 2. CONFIGURACIÓN DEL GRÁFICO
print("Generando mapa de eficiencia...")

# --- AQUI VIENE EL DISEÑO ---
# x: Partidos, y: Goles
# color: 'red' (puedes poner 'blue', 'green', 'hex codes'...)
# s: size (tamaño del punto). Ponemos 150 para que se vea bien.
# alpha: transparencia (0.7). Queda elegante si los puntos se superponen.
plt.scatter(tabla["Partidos"], tabla["Goles"], color="red", s=150, alpha=0.7)

# 3. PONER NOMBRES A LOS PUNTOS (Usamos tu conocimiento de bucles!)
# Recorremos la tabla fila por fila
for i in range(len(tabla)):
    # plt.text(x, y, texto) escribe en el gráfico
    plt.text(tabla["Partidos"][i], tabla["Goles"][i] + 0.5, tabla["Nombre"][i])

# 4. MAQUILLAJE FINAL
plt.title("Mapa de Eficiencia: Goles vs Partidos")
plt.xlabel("Partidos Jugados")
plt.ylabel("Goles Marcados")
plt.grid(True)  # Añade una rejilla de fondo (cuadrícula) para leer mejor

plt.show()
