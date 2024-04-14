# Crear y usar un diccionario en Python
# Imagina que tienes diferentes frutas y quieres recordar cuántas de cada una tienes en casa.

# Diccionario de frutas con la cantidad que tienes
inventario_de_frutas = {
    'manzana': 10,
    'banana': 5,
    'cereza': 20,
    'naranja': 8,
    'kiwi': 3
}

# Mostrar el diccionario completo
print('Inventario completo de frutas:', inventario_de_frutas)

# Acceder a un elemento específico en el diccionario: ¿Cuántas bananas tengo?
print('Cantidad de bananas:', inventario_de_frutas['banana'])

# Agregar una nueva fruta al diccionario
inventario_de_frutas['mango'] = 15
print('Inventario actualizado con mangos:', inventario_de_frutas)

# Cambiar la cantidad de una fruta existente
inventario_de_frutas['kiwi'] = 10
print('Cantidad actualizada de kiwis:', inventario_de_frutas['kiwi'])

# Eliminar una fruta del diccionario
del inventario_de_frutas['cereza']
print('Inventario después de eliminar las cerezas:', inventario_de_frutas)

# Mostrar qué pasa si intentamos agregar una clave duplicada
inventario_de_frutas['mango'] = 25
print('Actualización de la cantidad de mangos:', inventario_de_frutas)

# Crear un diccionario: Comenzamos definiendo un diccionario llamado inventario_de_frutas, 
# donde cada clave es el nombre de una fruta y el valor asociado es la cantidad que tienes de esa fruta.

# Mostrar el diccionario: Es útil mostrar el diccionario completo al principio para ver cómo está organizada la información.

# Acceder a elementos: Explicamos cómo obtener la cantidad de una fruta específica usando su nombre como clave. 
# Esto es como buscar una palabra en un diccionario para encontrar su definición.

# Agregar y modificar elementos: Mostramos cómo se pueden añadir nuevas frutas o cambiar la cantidad de frutas existentes. 
# Esto enseña que los diccionarios son mutables y pueden ser actualizados.

# Eliminar elementos: Finalmente, enseñamos cómo eliminar una fruta del diccionario, 
# lo que es útil para mantener el diccionario actualizado.

# Las claves en un diccionario siempre son únicas. Si se usa una clave que ya existe,
# el valor anterior se sobrescribe con el nuevo valor.