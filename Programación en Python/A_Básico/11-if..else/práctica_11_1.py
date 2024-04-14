# Estas estructuras son como tomar decisiones: 
# permiten que el programa elija hacer algo basado en si algo es verdadero o falso.

# Vamos a imaginar que variable1 y variable2 son las notas de dos exámenes

variable1 = 75
variable2 = 85

# Uso de if: Verificamos si la primera nota es mayor o igual a 60 (aprobado)
if variable1 >= 60:
    print("¡Felicidades! Aprobaste el primer examen.")

# Uso de elif: Verificamos si la segunda nota es exactamente 85
elif variable2 == 85:
    print("¡Perfecto! Tuviste una nota excelente en el segundo examen.")

# Uso de else: Si ninguna de las condiciones anteriores se cumple
else:
    print("Necesitas estudiar un poco más.")

# Podemos usar otra condición para comparar las dos notas
if variable1 > variable2:
    print("Tu primera nota es mayor que la segunda.")
elif variable1 < variable2:
    print("Tu segunda nota es mayor que la primera.")
else:
    print("Ambas notas son iguales.")


# Definición de variables: Primero, definimos dos variables (variable1 y variable2) 
# que representan notas de exámenes.

# Uso de if: Comprobamos si la variable1 (la primera nota) es suficiente para pasar (igual o mayor que 60). 
# Si es así, se ejecuta el código dentro de if y se muestra un mensaje positivo.

# Uso de elif: La instrucción elif (que significa "else if", o "si no") 
# permite verificar otra condición si la primera (if) no se cumple. 
# En este caso, verificamos si variable2 es exactamente 85. 
# Si es verdad, se muestra un mensaje sobre tener una nota excelente.

# Uso de else: Si ninguna de las condiciones anteriores se cumple (ni if ni elif), 
# el código dentro de else se ejecuta, dando un mensaje para motivar al estudiante a estudiar más.

# Comparación de las dos notas: Finalmente, comparamos las dos notas con otro conjunto 
# de if, elif, y else para determinar cuál es mayor o si son iguales, 
# mostrando el resultado correspondiente.