# 1. DEFINICIÓN (La receta):
# 'def' es la palabra clave. Significa: "Python, aprende este comando nuevo".
# 'calcular_promedio' es el nombre que le damos a la máquina.
# '(goles, partidos)' son los INGREDIENTES que necesita la máquina para arrancar.
def calcular_promedio(goles, partidos,):

    # 2. LA LÓGICA (El motor):
    # Dentro de la máquina, cogemos los ingredientes y hacemos la división.
    # El resultado se guarda temporalmente en 'promedio'.
    promedio = goles / partidos

    # 3. LA ENTREGA (El return):
    # ¡CRUCIAL! 'return' saca el dato de la función y te lo devuelve.
    # No lo imprime en pantalla, te lo "da en la mano" para que lo guardes en una variable.
    return promedio
# --- Aquí empieza el programa principal ---


# 4. PRIMERA LLAMADA (Vinicius):
# Llamamos a la función por su nombre 'calcular_promedio'.
# Le pasamos los datos reales: 15 (goles) y 20 (partidos).
# La máquina hace la división, hace el 'return', y guardamos el resultado en 'media_vini'.
media_vini = calcular_promedio(15, 20)

# 5. MOSTRAR RESULTADO 1:
# Usamos f-string para ver lo que hemos guardado en la variable.
print(f"El promedio de Vinicius es: {media_vini}")


# 6. SEGUNDA LLAMADA (Lewandowski - TU CÓDIGO):
# ¡Aquí está la magia de las funciones! REUTILIZAMOS la máquina.
# No escribimos la fórmula de dividir otra vez. Solo cambiamos los datos de entrada (25, 30).
# El resultado (0.8333...) se guarda en la nueva variable 'media_lewy'.
media_lewy = calcular_promedio(10, 20)

# 7. MOSTRAR RESULTADO 2:
print(f"El promedio de Lewandowski es: {media_lewy}")
