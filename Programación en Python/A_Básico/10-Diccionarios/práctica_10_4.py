# Crear y usar un diccionario anidado en Python
# Cada fruta tiene su propio diccionario con detalles como cantidad y color.

# Diccionario con detalles de cada fruta
inventario_de_frutas = {
    'manzana': {'cantidad': 10, 'color': 'rojo'},
    'banana': {'cantidad': 5, 'color': 'amarillo'},
    'cereza': {'cantidad': 20, 'color': 'rojo'},
    'naranja': {'cantidad': 8, 'color': 'naranja'},
    'kiwi': {'cantidad': 3, 'color': 'verde'}
}

# Mostrar el diccionario completo
print('Inventario completo de frutas:', inventario_de_frutas)

# Acceder a una fruta específica y mostrar sus detalles
fruta_seleccionada = 'naranja'
detalles_de_la_fruta = inventario_de_frutas[fruta_seleccionada]
print(f'Detalles de la {fruta_seleccionada}:', detalles_de_la_fruta)

# Crear el diccionario anidado: Se define un diccionario inventario_de_frutas 
# donde cada clave es el nombre de una fruta y el valor asociado es otro diccionario 
# que incluye la cantidad de frutas disponibles y su color.

# Mostrar el diccionario completo: Es importante que vean la estructura completa 
# para comprender cómo están organizados los datos.

# Acceder a detalles específicos de una fruta: Se muestra cómo acceder 
# a la información de una fruta específica, en este caso la naranja, 
# para ver su cantidad y color. Esto demuestra cómo navegar por diccionarios anidados.