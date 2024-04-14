# Ordenar listas en Python
# Podemos usar el método sort() para ordenar los elementos de una lista en orden alfabético.

# Tenemos una lista de frutas
frutas = ['manzana', 'banana', 'cereza', 'naranja', 'kiwi']

# Mostrar la lista original
print('Lista original de frutas:', frutas)

# Ordenar la lista
frutas.sort()
print('Lista de frutas ordenada:', frutas)

# Si queremos la lista en orden inverso, podemos hacerlo de esta forma:
frutas.sort(reverse=True)
print('Lista de frutas en orden inverso:', frutas)

# Ordenar la lista alfabéticamente: Utilizamos el método sort() 
# que automáticamente ordena los elementos de la lista de la A a la Z.

# Ordenar la lista en orden inverso: Usando el mismo método sort() pero con el argumento reverse=True, 
# podemos ordenar la lista en orden inverso, de la Z a la A.