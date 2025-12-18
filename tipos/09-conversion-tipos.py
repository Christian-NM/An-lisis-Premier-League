x = input("")  # Solicita al usuario un valor por teclado (siempre es string)
print(type(x))  # Imprime el tipo de dato de x (str)

x = int(x)  # Convierte x a entero
print(type(x))  # Imprime el tipo de dato de x (int)

y = input("")  # Solicita al usuario otro valor por teclado (string)
print(type(y))  # Imprime el tipo de dato de y (str)

y = float(y)  # Convierte y a flotante
print(type(y))  # Imprime el tipo de dato de y (float)

z = x + y  # Suma x (int) y y (float)
print(z)  # Imprime el resultado de la suma
