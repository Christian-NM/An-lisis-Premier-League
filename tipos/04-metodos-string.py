animal = "  perro feliz  "

# Convierte todos los caracteres a mayúsculas
print(animal.upper())

# Convierte todos los caracteres a minúsculas
print(animal.lower())

# Convierte el primer carácter a mayúscula y el resto a minúsculas
print(animal.capitalize())

# Convierte la primera letra de cada palabra a mayúscula
print(animal.title())

# Elimina los espacios al inicio y al final de la cadena
print(animal.strip())  # La variable original no se modifica

# Elimina los espacios y luego capitaliza el primer carácter
print(animal.strip().capitalize())

# Elimina los espacios solo al final de la cadena
print(animal.rstrip())

# Elimina los espacios solo al inicio de la cadena
print(animal.lstrip())

# Busca la subcadena "Fe" y devuelve el índice donde inicia, o -1 si no la encuentra
print(animal.find("Fe"))

# Reemplaza la subcadena "fe" por "j" en la cadena
print(animal.replace("fe", "j"))

# Verifica si "fe" está en la cadena (True/False)
print("fe" in animal)

# Verifica si "fe" no está en la cadena (True/False)
print("fe" not in animal)

# Cuenta cuántas veces aparece la subcadena "e" en la cadena
print(animal.count("e"))

# Verifica si la cadena comienza con "perro"
print(animal.startswith("perro"))

# Verifica si la cadena termina con "feliz"
print(animal.endswith("feliz"))
