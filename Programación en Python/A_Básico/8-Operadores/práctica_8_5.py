# operadores de identidad
# Los operadores de identidad se utilizan para comparar las identidades de los objetos en Python.

# Operador is
# Verifica si dos variables apuntan al mismo objeto
lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]

es_mismo_objeto = lista1 is lista2
print('¿Lista1 es el mismo objeto que lista2?', es_mismo_objeto)  # Esto imprimirá: True

es_mismo_objeto = lista1 is lista3
print('¿Lista1 es el mismo objeto que lista3?', es_mismo_objeto)  # Esto imprimirá: False

# Operador is not
# Verifica si dos variables no apuntan al mismo objeto
no_es_mismo_objeto = lista1 is not lista3
print('¿Lista1 no es el mismo objeto que lista3?', no_es_mismo_objeto)  # Esto imprimirá: True

# is: Este operador verifica si dos variables apuntan exactamente al mismo objeto, 
# no solo si son iguales en valor. En el ejemplo, lista1 y lista2 son el mismo objeto porque lista2 es asignada como lista1.
# Sin embargo, lista3 tiene los mismos elementos pero es un objeto diferente creado separadamente.
# is not: Este operador es lo contrario de is; verifica si dos variables no apuntan al mismo objeto. 
# Aunque lista1 y lista3 tienen los mismos contenidos, son diferentes objetos, y por eso el resultado es True.