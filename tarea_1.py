# 1. TIPO TEXTO (String):
# Creamos la caja 'nombre'. Usamos comillas "" para decirle a Python que esto es texto.
nombre = "Christian"

# 2. TIPO ENTERO (Integer):
# Creamos la caja 'edad'. NO usamos comillas porque queremos que sea un número para poder sumar o restar.
edad = 37

# 3. TIPO DECIMAL (Float):
# Creamos la caja 'altura'. En programación, los decimales se separan con PUNTO, no con coma.
altura = 1.78

# 4. TIPO BOOLEANO (Boolean):
# Creamos la caja 'estudiante'. Esto es un interruptor. Solo puede ser True (Verdadero) o False (Falso).
# Es vital para filtros: ¿Es estudiante? SÍ.
estudiante = True


# 5. SALIDA POR PANTALLA (f-string):
# La 'f' al principio activa el modo "formato".
# Le dice a Python: "Dentro de este texto, si ves algo entre llaves {}, búscame esa variable y pon su valor".
print("El usuario {nombre} tiene {edad} años, mide {altura} y es estudiante")
