# Copiar listas en Python
# A veces necesitamos hacer una copia de una lista para trabajar con ella sin cambiar la original.

# Tenemos una lista de frutas
frutas_original = ['manzana', 'banana', 'cereza', 'naranja', 'kiwi']

# Mostrar la lista original
print('Lista original de frutas:', frutas_original)

# Copiar la lista usando el método copy()
frutas_copiada = frutas_original.copy()
print('Lista copiada de frutas:', frutas_copiada)

# Modificar la lista copiada
frutas_copiada.append('mango')
print('Lista copiada modificada (agregamos mango):', frutas_copiada)

# Mostrar la lista original para ver que no ha cambiado
print('La lista original sigue igual:', frutas_original)

# Lista original: Se crea una lista de frutas 

# Copiar la lista: Utilizamos el método copy() para hacer una copia exacta de la lista original. 
# Esta nueva lista es completamente independiente de la original.

# Modificar la lista copiada: Agregamos un nuevo elemento a la lista copiada para demostrar 
# que los cambios en la copia no afectan la lista original.

# Comparar con la lista original: Finalmente, mostramos nuevamente la lista original 
# para confirmar que sigue igual a pesar de los cambios en la copia.
