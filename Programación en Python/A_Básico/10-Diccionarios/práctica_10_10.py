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

# Usamos update para agregar nuevas frutas al diccionario
inventario_de_frutas.update({
    'mango': {'cantidad': 12, 'color': 'amarillo'},
    'piña': {'cantidad': 5, 'color': 'marrón'}
})

# Mostramos el inventario después de agregar nuevas frutas
print("\nInventario después de agregar nuevas frutas:")
for fruta, detalles in inventario_de_frutas.items():
    print(f"{fruta.capitalize()}: {detalles['cantidad']} unidades, color {detalles['color']}")

# Inicialización del diccionario: Comenzamos con un diccionario inventario_de_frutas 
# que ya contiene algunas frutas con su respectiva cantidad y color.

# Imprimir el inventario original: Para que vean claramente 
# lo que contiene el diccionario antes de cualquier cambio.

# Agregar nuevos items usando update():

# Nuevas frutas: Agregamos 'mango' y 'piña' al diccionario. 
# El método update() es muy útil porque permite agregar múltiples items a la vez, 
# y si las frutas ya existieran en el diccionario, sus detalles serían actualizados.
# Mostrar los cambios: Finalmente, imprimimos el diccionario actualizado 
# para ver cómo han sido agregadas las nuevas frutas.
