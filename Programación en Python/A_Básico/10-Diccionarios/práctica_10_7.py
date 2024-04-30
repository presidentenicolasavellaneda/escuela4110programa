# Diccionario con detalles de cada fruta
inventario_de_frutas = {
    'manzana': {'cantidad': 10, 'color': 'rojo'},
    'banana': {'cantidad': 5, 'color': 'amarillo'},
    'cereza': {'cantidad': 20, 'color': 'rojo'},
    'naranja': {'cantidad': 8, 'color': 'naranja'},
    'kiwi': {'cantidad': 3, 'color': 'verde'}
}

# Obtener los valores del diccionario
valores_de_frutas = inventario_de_frutas.values()
print('Los detalles de las frutas disponibles en el inventario son:')
for detalles in valores_de_frutas:
    print(detalles)

# Diccionario anidado definido: Usamos el mismo diccionario de antes que almacena información sobre varias frutas, 
# cada una representada como una clave con un diccionario como valor que incluye la cantidad y el color.

# Obtener y mostrar valores: Usamos el método .values() para extraer todos los valores 
# (que son diccionarios en este caso) del diccionario principal. 
# Estos valores son mostrados uno por uno en un bucle, 
# lo que permite ver todos los detalles disponibles de cada fruta en el inventario.