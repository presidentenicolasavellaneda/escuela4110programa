# Diccionario con detalles de cada fruta
inventario_de_frutas = {
    'manzana': {'cantidad': 10, 'color': 'rojo'},
    'banana': {'cantidad': 5, 'color': 'amarillo'},
    'cereza': {'cantidad': 20, 'color': 'rojo'},
    'naranja': {'cantidad': 8, 'color': 'naranja'}
}

# Mostramos el inventario original
print("Inventario original:")
for fruta, detalles in inventario_de_frutas.items():
    print(f"{fruta.capitalize()}: {detalles['cantidad']} unidades, color {detalles['color']}")

# Removemos 'cereza' del diccionario usando pop()
fruta_eliminada = inventario_de_frutas.pop('cereza', None)

# Chequeamos si la fruta fue eliminada correctamente
if fruta_eliminada:
    print(f"\nSe eliminó la cereza con éxito: {fruta_eliminada}")
else:
    print("\nLa fruta no se encontró en el inventario.")

# Mostramos el inventario después de remover la fruta
print("\nInventario después de remover una fruta:")
for fruta, detalles in inventario_de_frutas.items():
    print(f"{fruta.capitalize()}: {detalles['cantidad']} unidades, color {detalles['color']}")

# Inicialización del diccionario: El diccionario inventario_de_frutas inicial 
# contiene frutas con su respectiva cantidad y color.

# Imprimir el inventario original: Esto da una idea clara de lo que contiene 
# el diccionario antes de realizar cualquier cambio.

# Uso de pop() para remover un elemento:

# Remover 'cereza': Usamos pop('cereza', None). Aquí, 'cereza' es la clave que queremos eliminar, 
# y None es un valor por defecto que se devuelve si la clave no se encuentra en el diccionario. 
# Esto ayuda a evitar errores si intentamos eliminar una clave que no existe.
# Verificación y mensaje: Se imprime un mensaje para confirmar que la fruta fue eliminada correctamente 
# o para informar que la fruta no se encontró.

# Mostrar los cambios: Finalmente, imprimimos el diccionario 
# para ver cómo ha sido modificado después de remover la fruta.