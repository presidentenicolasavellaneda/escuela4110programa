# Inicializamos el contador
contador = 1

# Configuramos el bucle while para ejecutarse mientras el contador sea menor o igual a 5
while contador <= 5:
    print("El contador está en:", contador)
    contador += 1  # Incrementamos el contador en 1 en cada iteración
else:
    # Este bloque se ejecuta después de que el bucle while completa su ejecución normalmente
    print("El bucle ha terminado sin interrupciones y el contador es mayor que 5.")

# Inicialización del contador: Comienza con contador = 1.
# Condiciones del bucle while: 
# La condición while contador <= 5 permite que el bucle se ejecute mientras el contador no supere 5.
# Impresión del contador: 
# En cada iteración, se imprime el valor actual del contador.
# Incremento del contador: 
# En cada iteración se incrementa el contador en 1.
# Bloque else: Una vez que el contador supera el valor 5 y el bucle while finaliza normalmente, 
# se ejecuta el bloque de código bajo else.
# Mensaje de finalización: Se imprime un mensaje que indica que el bucle ha terminado sin interrupciones.