# Bucles en Python
# Un bucle nos permite realizar la misma acción con cada elemento de una lista.

# Tenemos una lista de frutas
frutas = ['manzana', 'banana', 'cereza', 'naranja', 'kiwi']

# Usar un bucle 'for' para imprimir cada fruta de la lista
print('Lista de frutas:')
for fruta in frutas:
    print(fruta)

# Usar un bucle 'for' para hacer algo más con cada fruta
print('\nFrutas con mensaje:')
for fruta in frutas:
    mensaje = "Me gusta la " + fruta
    print(mensaje)

# Contar cuántas letras tiene el nombre de cada fruta
print('\nNúmero de letras de cada fruta:')
for fruta in frutas:
    longitud = len(fruta)
    print('La fruta', fruta, 'tiene', longitud, 'letras.')

# Bucle for para imprimir elementos: Primero, se imprime cada fruta en la lista. 
# El bucle for recorre la lista frutas, tomando una fruta a la vez y la imprime.

# Bucle for para formar un mensaje: Luego, usamos el bucle para formar un mensaje simple con cada fruta. 
# Esto muestra cómo se puede manipular y utilizar cada elemento de la lista en una sentencia.

# Contar letras en cada nombre de fruta: Finalmente, mostramos cómo contar las letras de cada nombre de fruta usando len(), 
# lo que ayuda a introducir conceptos básicos de cadenas y contar.
