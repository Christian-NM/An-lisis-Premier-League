# 1. ENTRADA Y CONVERSIÓN:
# Pedimos el dato con input(). Como input devuelve texto, lo envolvemos en int()
# para convertirlo a número entero. Necesitamos números para poder comparar (mayor que, menor que...).
goles = int(input("Cuántos goles has marcado hoy: "))

# 2. PRIMER FILTRO (El más restrictivo):
# Python pregunta: "¿El número es 4 o más?".
# Si es SÍ: Entra, imprime el mensaje y SE ACABA el bloque (ignora el resto de elif/else).
if goles >= 4:
    print("Eres una estrella del fútbol!!!")

# 3. SEGUNDO FILTRO (elif = "else if" / "si no, pero..."):
# Si no era >= 4, Python baja aquí. Pregunta: "¿Es EXACTAMENTE 3?".
# Fíjate en el doble igual (==). Un '=' es para asignar valor, dos '==' son para comparar.
elif goles == 3:
    print("Hat trick! Te llevas el balón a casa")

# 4. TERCER FILTRO:
# Si no es >= 4 ni es 3, Python baja aquí.
# Pregunta: "¿Es mayor que 0?".
# Por lógica, si llega aquí solo pueden ser 1 o 2 goles.
elif goles > 0:
    print("Buen partido, has sumado al marcador")

# 5. CUARTO FILTRO:
# Si nada de lo anterior funcionó, pregunta: "¿Es cero?".
elif goles == 0:
    print("A seguir entrenando, hoy no ha habido suerte de cara a puerta")

# 6. EL CARRY-ALL (else = "si no..."):
# Si el número no ha encajado en NINGUNA de las condiciones anteriores (es decir, es negativo).
# El 'else' no lleva condición, atrapa todo lo que sobra.
else:
    print("Error: No puedes marcar un número negativo de goles")
