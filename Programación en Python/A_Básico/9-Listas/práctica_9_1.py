# Listas en Python
# Una lista es una colección de elementos que pueden ser modificados.
# Podemos usar listas para guardar un conjunto de elementos, como nombres de frutas.

# Crear una lista de frutas
frutas = ['manzana', 'banana', 'cereza']
print('Lista de frutas:', frutas)

# Acceder a elementos de la lista
# Podemos obtener cualquier elemento de la lista usando su índice. Recuerda que en Python, el índice comienza en 0.
primera_fruta = frutas[0]
print('La primera fruta es:', primera_fruta)  # Esto imprimirá: manzana

# Añadir un elemento al final de la lista
frutas.append('naranja')
print('Lista de frutas después de añadir naranja:', frutas)

# Eliminar un elemento de la lista
frutas.remove('banana')
print('Lista de frutas después de eliminar banana:', frutas)

# Insertar un elemento en una posición específica
frutas.insert(1, 'kiwi')
print('Lista de frutas después de insertar kiwi en la posición 2:', frutas)

# Contar elementos en la lista
numero_de_frutas = len(frutas)
print('Número de frutas en la lista:', numero_de_frutas)

# Creación de una lista: Iniciamos con una lista de frutas. 
#Cada fruta es un elemento en la lista, y todos juntos están encerrados en corchetes [].
# Acceder a elementos: Usamos índices para obtener elementos específicos de la lista. 
# El índice empieza en cero, por lo que frutas[0] es 'manzana'.
# Agregar elementos: Con append(), podemos añadir nuevos elementos al final de la lista.
# Eliminar elementos: remove() nos permite quitar un elemento por su valor.
# Insertar elementos: insert() añade un elemento en una posición específica.
# Contar elementos: len() nos da el número total de elementos en la lista.