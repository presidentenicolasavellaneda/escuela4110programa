# Diccionario con detalles de cada fruta
inventario_de_frutas = {
    'manzana': {'cantidad': 10, 'color': 'rojo'},
    'banana': {'cantidad': 5, 'color': 'amarillo'},
    'cereza': {'cantidad': 20, 'color': 'rojo'},
    'naranja': {'cantidad': 8, 'color': 'naranja'},
    'kiwi': {'cantidad': 3, 'color': 'verde'}
}

# Usar get() para obtener detalles de una fruta
fruta_seleccionada = 'naranja'
detalles_de_la_fruta = inventario_de_frutas.get(fruta_seleccionada, 'No hay información disponible')
print(f'Detalles de la {fruta_seleccionada}:', detalles_de_la_fruta)

# Intentar acceder a una fruta que no está en el inventario
fruta_inexistente = 'mango'
detalles_fruta_inexistente = inventario_de_frutas.get(fruta_inexistente, 'No hay información disponible')
print(f'Detalles del {fruta_inexistente}:', detalles_fruta_inexistente)

# Diccionario anidado definido: Incluimos los detalles de algunas frutas en un diccionario 
# donde cada clave es el nombre de la fruta y el valor es otro diccionario con detalles como la cantidad y el color.

# Uso de get() para acceder a detalles seguros: Usamos get() para buscar detalles de la 'naranja'. 
# Si la fruta existe, muestra sus detalles. Usamos un valor por defecto de "No hay información disponible" 
# para evitar errores si la clave no existe.

# Manejo de claves que no existen: Intentamos acceder a una fruta ('mango') 
# que no está en el diccionario. En lugar de causar un error, 
# get() devuelve el mensaje de que no hay información disponible, 
# demostrando así su utilidad para manejar casos donde la clave podría no estar presente.