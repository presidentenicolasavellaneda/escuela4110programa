# Vamos a buscar el número 5 en una lista de números
numeros = [1, 2, 3, 4, 6, 7, 8, 9, 10]

print("Vamos a buscar el número 5 en la lista...")

for numero in numeros:
    if numero == 5:
        print("¡Hemos encontrado el número 5!")
        break
else:
    print("No hemos encontrado el número 5 en la lista.")

print("Hemos terminado de buscar en la lista.")

# Lista de Números: 
# Definimos una lista de números del 1 al 10, excepto el 5.
# Mensaje Inicial: 
# Antes del bucle, imprimimos que vamos a empezar a buscar el número 5.
# Bucle For: 
# El bucle recorre cada elemento en la lista.
# Condición If: 
# Si encontramos el número 5, imprimimos que lo hemos encontrado y usamos break para salir del bucle.
# Bloque Else: Si el bucle completa todas sus iteraciones sin encontrar el 5 y sin que se ejecute el break, 
# se ejecutará el bloque else, donde imprimimos que el número 5 no está en la lista.
# Mensaje Final: Indicamos que hemos terminado de buscar en la lista.