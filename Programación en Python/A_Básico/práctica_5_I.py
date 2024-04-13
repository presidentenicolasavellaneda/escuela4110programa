# Números en python

# hay tres tipos de números en python:
# enteros
x = 10

# flotantes
y = 2.8

# complejos
z = 1j

# puedes usar la función type 
# para saber qué tipo de dato es cada una
# de las variables anteriores

print('la variable x es de tipo ',type(x))
print('la variable y es de tipo ',type(y))
print('la variable z es de tipo ',type(z))

# puedes convertir los números de un tipo a otro tipo
# usando lo que se llama 'Type Conversion'
a1 = 1
b1 = 2.8
c1 = 2j

# convierto de entero a flotante
a2 = float(a1)
b2 = int(b1)

# los imprimo
print(a2)
print(b2)