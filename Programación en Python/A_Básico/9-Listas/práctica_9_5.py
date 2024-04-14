# Unir listas en Python
# A veces queremos juntar dos listas para tener todos los elementos en una sola.

# Primera lista de frutas
frutas1 = ['manzana', 'banana', 'cereza']

# Segunda lista de frutas
frutas2 = ['naranja', 'kiwi', 'mango']

# Mostrar ambas listas originales
print('Primera lista de frutas:', frutas1)
print('Segunda lista de frutas:', frutas2)

# Unir las dos listas usando el operador +
frutas_unidas = frutas1 + frutas2
print('Lista unida de frutas:', frutas_unidas)

# Otra forma de unir listas es usando el método extend()
frutas1.extend(frutas2)
print('Lista de frutas después de usar extend():', frutas1)

# Listas originales: Se crean dos listas separadas de frutas. Es útil mostrar ambas listas para que vean claramente los elementos que cada una contiene.

# Unir listas con +: La primera forma de unir las listas es utilizando el operador +, que combina las listas 
# y crea una nueva.

# Usar extend(): El método extend() es otra forma de unir listas. A diferencia del operador +, 
# extend() añade los elementos de la segunda lista al final de la primera lista sin crear una nueva lista.