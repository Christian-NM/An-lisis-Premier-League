n1 = input("Ingresa el primer número")
n2 = input("Ingresa el segundo número")

n1 = int(n1)
n2 = int(n2)
suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2


mensaje = f"""

Para los numeros {n1} y {n2}:  

La suma es {suma}
La resta es {resta}
La multiplicacion es {multiplicacion}
La division es {division}

"""
print(mensaje)
