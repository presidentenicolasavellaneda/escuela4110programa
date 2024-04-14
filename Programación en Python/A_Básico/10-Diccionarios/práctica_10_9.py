# Diccionario con detalles de cada fruta

# Definición del diccionario: Continuamos utilizando el mismo diccionario de frutas 
# que incluye detalles como la cantidad y el color de cada fruta.

# Mostrar la cantidad actual: Antes de actualizar el diccionario, mostramos la cantidad actual de manzanas 
# para ver el valor antes de la actualización.

# Actualizar el elemento: Modificamos directamente el valor de la cantidad de manzanas en el diccionario. 
# Aquí, cambiamos la cantidad de 10 a 15.

# Mostrar la cantidad actualizada: Después de la actualización, 
# mostramos el nuevo valor para confirmar que el diccionario ha sido actualizado correctamente.

inventario_de_frutas = {
    'manzana': {'cantidad': 10, 'color': 'rojo'},
    'banana': {'cantidad': 5, 'color': 'amarillo'},
    'cereza': {'cantidad': 20, 'color': 'rojo'},
    'naranja': {'cantidad': 8, 'color': 'naranja'},
    'kiwi': {'cantidad': 3, 'color': 'verde'}
}

# Mostramos el inventario actual de manzanas
print(f"La cantidad actual de manzanas es: {inventario_de_frutas['manzana']['cantidad']}")

# Actualizamos la cantidad de manzanas
inventario_de_frutas['manzana']['cantidad'] = 15

# Mostramos el inventario actualizado de manzanas
print(f"La cantidad actualizada de manzanas es: {inventario_de_frutas['manzana']['cantidad']}")

###########################################################################################################

# otra forma de actualizar

# Actualizamos las cantidades de manzanas y bananas usando update
inventario_de_frutas.update({
    'manzana': {'cantidad': 35, 'color': 'verde'},
    'banana': {'cantidad': 10, 'color': 'amarillo'}
})

# Mostramos el inventario actualizado de manzanas y bananas
print(f"La cantidad actualizada de manzanas es: {inventario_de_frutas['manzana']['cantidad']}")
print(f"La cantidad actualizada de bananas es: {inventario_de_frutas['banana']['cantidad']}")
print(f"El nuevo color de las manzanas es: {inventario_de_frutas['manzana']['color']}")