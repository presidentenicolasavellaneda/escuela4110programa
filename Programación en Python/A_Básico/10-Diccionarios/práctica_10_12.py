# Diccionario original con detalles de frutas
inventario_de_frutas = {
    'manzana': {'cantidad': 10, 'color': 'rojo'},
    'banana': {'cantidad': 5, 'color': 'amarillo'},
    'cereza': {'cantidad': 20, 'color': 'rojo'}
}

# Mostramos el diccionario original
print("Inventario original:")
for fruta, detalles in inventario_de_frutas.items():
    print(f"{fruta.capitalize()}: {detalles['cantidad']} unidades, color {detalles['color']}")

# Copiamos el diccionario usando el método copy()
copia_inventario = inventario_de_frutas.copy()

# Mostramos la copia para verificar que se ha copiado correctamente
print("\nCopia del inventario:")
for fruta, detalles in copia_inventario.items():
    print(f"{fruta.capitalize()}: {detalles['cantidad']} unidades, color {detalles['color']}")

# Modificamos la copia sin afectar el original
copia_inventario['manzana']['cantidad'] = 15

# Mostramos ambos diccionarios para ver la diferencia después de modificar la copia
print("\nInventario original después de modificar la copia:")
for fruta, detalles in inventario_de_frutas.items():
    print(f"{fruta.capitalize()}: {detalles['cantidad']} unidades, color {detalles['color']}")

print("\nCopia del inventario después de modificar:")
for fruta, detalles in copia_inventario.items():
    print(f"{fruta.capitalize()}: {detalles['cantidad']} unidades, color {detalles['color']}")

# Inicialización del diccionario: Creamos un diccionario que almacena información sobre diferentes frutas, 
# como la cantidad y el color.

# Impresión del diccionario original

# Copiar el diccionario: Usamos el método .copy() para crear una copia del diccionario original. 
# Este método es seguro porque crea una nueva instancia del diccionario sin vincularlo al original.

# Modificar la copia: Cambiamos el valor en la copia del diccionario para demostrar que esta operación 
# no afecta al diccionario original.

# Verificar cambios: Imprimimos ambos diccionarios después de la modificación 
# para observar que el original permanece sin cambios mientras que la copia sí refleja las modificaciones.