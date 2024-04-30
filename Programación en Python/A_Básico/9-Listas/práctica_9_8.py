# Usar index() para encontrar la posición de un elemento en una lista
# Imagina que quieres saber en qué posición se encuentra la primera naranja en tu lista de frutas.

# Lista de frutas
frutas = ['manzana', 'banana', 'cereza', 'naranja', 'kiwi', 'manzana', 'banana', 'naranja']

# Mostrar la lista de frutas
print('Lista de frutas:', frutas)

# Encontrar la posición de la primera naranja
posicion_naranja = frutas.index('naranja')
print('La primera naranja está en la posición:', posicion_naranja)

# Si estás buscando la posición de una fruta que no está en la lista, Python mostrará un error.
# Para evitar errores, primero puedes verificar si la fruta está en la lista:
fruta_buscada = 'mango'
if fruta_buscada in frutas:
    posicion_fruta = frutas.index(fruta_buscada)
    print('La primera', fruta_buscada, 'está en la posición:', posicion_fruta)
else:
    print(fruta_buscada, 'no está en la lista de frutas.')

# Lista de frutas: Primero, se define una lista con varias frutas, algunas de las cuales están repetidas, 
# para mostrar cómo funciona el método index().

# Uso de index(): Se utiliza el método para encontrar la posición de la primera 'naranja' en la lista. 
# El resultado se imprime para mostrar dónde se encuentra esta fruta en la lista.

# Manejo de errores: Se incluye un ejemplo de cómo evitar errores al buscar un elemento que no está en la lista, 
# utilizando una condición if. Esto enseña a escribir código que previene fallos.
