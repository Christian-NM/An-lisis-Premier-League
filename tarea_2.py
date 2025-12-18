# 1. ENTRADA DE TEXTO (input):
# La función input() detiene el programa y espera a que escribas algo.
# Todo lo que escribas se guarda en la variable 'nombre' como TEXTO (string).
nombre = input("Dime tu nombre: ")

# 2. CONVERSIÓN A ENTERO (int):
# input() devuelve texto, pero las horas son números.
# 'int()' envuelve al input para transformar ese texto (ej: "40") en un número entero (40) para poder multiplicar después.
horas = int(input("Cuantas horas has trabajado este mes: "))

# 3. CONVERSIÓN A DECIMAL (float):
# El precio puede tener céntimos (ej: 15.50), así que usamos 'float()' en vez de 'int()'.
# Si usáramos int(), perderíamos los céntimos.
precio = float(input("Precio por hora trabajada: "))

# 4. OPERACIÓN MATEMÁTICA:
# Ahora que 'horas' y 'precio' son números (no texto), podemos multiplicarlos con el asterisco (*).
# El resultado se guarda en la caja 'total'.
total = horas * precio

# 5. SALIDA CON F-STRING:
# Usamos la f"" para mezclar texto fijo ("Hola") con el contenido de tus variables ({nombre}, {total}).
# Fíjate que aquí ya corregiste el error del espacio después de "Hola".
print(f"Hola {nombre}, has trabajado {horas} horas este mes y tu salario es de {total} euros.")
