# Crear y usar un diccionario en Python
# Aquí tenemos un diccionario con diferentes tipos de datos. No solo números, también listas!

# Diccionario de frutas con la cantidad que tienes y sus colores
inventario_de_frutas = {
    'manzana': 10,
    'banana': 5,
    'cereza': 20,
    'naranja': 8,
    'kiwi': 3,
    'colores': ['rojo', 'amarillo', 'rojo', 'naranja', 'verde']
}

# Mostrar el diccionario completo
print('Inventario completo de frutas:', inventario_de_frutas)

# Mostrar solo los colores de las frutas
print('Colores de las frutas:', inventario_de_frutas['colores'])

# Expansión del diccionario: Agregamos una nueva clave llamada colores que almacena una lista de colores 
# asociados con las frutas. Cada color en la lista puede corresponder a la fruta en el mismo orden 
# de aparición en el diccionario.

# Mostrar el diccionario completo: Es útil mostrar todo el contenido 
# del diccionario para que los niños vean cómo se estructura la información.

# Acceder a una clave específica: Mostramos cómo acceder a la lista de colores 
# utilizando la clave colores del diccionario, lo que permite ver específicamente los colores almacenados.
