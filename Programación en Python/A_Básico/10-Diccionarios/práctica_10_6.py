# Diccionario con detalles de cada fruta
inventario_de_frutas = {
    'manzana': {'cantidad': 10, 'color': 'rojo'},
    'banana': {'cantidad': 5, 'color': 'amarillo'},
    'cereza': {'cantidad': 20, 'color': 'rojo'},
    'naranja': {'cantidad': 8, 'color': 'naranja'},
    'kiwi': {'cantidad': 3, 'color': 'verde'}
}

# Obtener las claves del diccionario
claves_de_frutas = inventario_de_frutas.keys()
print('Las frutas disponibles en el inventario son:', list(claves_de_frutas))

# Diccionario anidado definido: El diccionario inventario_de_frutas contiene varias frutas como claves, 
# y cada clave tiene asociado un diccionario con detalles como la cantidad y el color de la fruta.

# Obtener y mostrar claves: Usamos el método .keys() para obtener todas las claves del diccionario inventario_de_frutas, 
# es decir, los nombres de las frutas. Luego convertimos estas claves a una lista para imprimirlos de forma más legible. 
# Esto muestra cómo pueden ver qué frutas están disponibles en el inventario.