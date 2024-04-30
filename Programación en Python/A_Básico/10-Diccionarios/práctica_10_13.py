# Diccionario de frutas, donde cada clave es una fruta y el valor es otro diccionario con detalles
diccionario_de_frutas = {
    'manzana': {'cantidad': 10, 'color': 'rojo'},
    'banana': {'cantidad': 5, 'color': 'amarillo'},
    'cereza': {'cantidad': 20, 'color': 'rojo'}
}

# Mostramos la información de cada fruta en el diccionario
print("Información de frutas:")
for fruta, detalles in diccionario_de_frutas.items():
    print(f"La fruta {fruta} tiene los siguientes detalles:")
    # Iteramos dentro del diccionario anidado para mostrar cada detalle
    for detalle, valor in detalles.items():
        print(f"  {detalle.capitalize()}: {valor}")

# Ejemplo de cómo acceder a un detalle específico:
# Vamos a mostrar cuántas manzanas hay
cantidad_manzanas = diccionario_de_frutas['manzana']['cantidad']
print(f"\nCantidad de manzanas en inventario: {cantidad_manzanas}")

# Creación del diccionario anidado: El diccionario diccionario_de_frutas contiene varias frutas como claves. 
# Cada clave apunta a otro diccionario que contiene detalles como la cantidad y el color de la fruta.

# Iterar sobre el diccionario principal: Usamos un bucle for para recorrer cada pareja clave-valor en el diccionario principal. 
# La clave es el nombre de la fruta y el valor es otro diccionario.

# Iterar sobre los diccionarios anidados: Dentro de cada iteración principal, 
# hacemos otro bucle for para recorrer el diccionario de detalles de cada fruta. 
# Así mostramos cada detalle (como cantidad y color).

# Acceso directo a un detalle específico: Al final, 
# mostramos cómo acceder directamente a un detalle específico de una fruta. 
# En este caso, mostramos la cantidad de manzanas directamente accediendo 
# al valor correspondiente en el diccionario anidado.