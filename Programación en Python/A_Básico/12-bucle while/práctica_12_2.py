# Inicializamos el contador
contador = 1

# Configuramos el bucle while para ejecutarse mientras el contador sea menor o igual a 5
while contador <= 5:
    print("El contador está en:", contador)
    
    # Si el contador llega a 3, salimos del bucle con break
    if contador == 3:
        print("El contador ha llegado a 3, vamos a detenernos aquí.")
        break

    # Incrementamos el contador en 1 en cada iteración
    contador += 1

print("Hemos salido del bucle.")

# Inicialización del contador: Comienza con contador = 1.
# Condiciones del bucle while: 
# La condición while contador <= 5 permite que el bucle se ejecute mientras el contador no supere 5.
# Condición de salida con break: 
# Dentro del bucle, hay una condición if contador == 3 que verifica si el contador ha alcanzado el valor 3. 
# Si es así, imprime un mensaje y ejecuta break, lo cual inmediatamente detiene el bucle.
# Incremento del contador: Si no se cumple la condición del if, el contador se incrementa en 1.
# Mensaje de salida del bucle: 
# Después de salir del bucle, se imprime un mensaje final que indica que hemos salido del bucle.