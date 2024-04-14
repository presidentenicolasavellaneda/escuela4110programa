# Inicializamos el contador
contador = 1

# Configuramos el bucle while para ejecutarse mientras el contador sea menor o igual a 5
while contador <= 5:
    # Si el contador llega a 3, no lo mostramos y continuamos con el siguiente número
    if contador == 3:
        contador += 1  # Incrementamos el contador antes de continuar
        continue       # Continuamos con la siguiente iteración sin ejecutar el código restante del bucle

    print("El contador está en:", contador)

    # Incrementamos el contador en 1 en cada iteración
    contador += 1

print("Hemos completado el conteo, omitiendo el número 3.")

# Inicialización del contador: Comienza con contador = 1.
# Condiciones del bucle while: 
# La condición while contador <= 5 permite que el bucle se ejecute mientras el contador no supere 5.
# Condicional con continue: 
# Si el contador llega a 3, no se ejecuta el print para ese número, 
# y se continúa con la siguiente iteración del bucle. 
# Importante notar que se debe incrementar el contador antes del continue para evitar un bucle infinito.
# Impresión del contador: 
# Si no se cumple la condición del if, el contador se imprime.
# Incremento del contador: 
# En cada iteración se incrementa el contador en 1.
# Mensaje de salida del bucle: 
# Después de completar el bucle, se imprime un mensaje final que indica que se ha omitido el número 3 
# y completado el conteo.