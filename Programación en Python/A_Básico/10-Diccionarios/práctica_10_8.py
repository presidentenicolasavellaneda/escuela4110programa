# Diccionario con detalles de cada fruta
inventario_de_frutas = {
    'manzana': {'cantidad': 10, 'color': 'rojo'},
    'banana': {'cantidad': 5, 'color': 'amarillo'},
    'cereza': {'cantidad': 20, 'color': 'rojo'},
    'naranja': {'cantidad': 8, 'color': 'naranja'},
    'kiwi': {'cantidad': 3, 'color': 'verde'}
}

# Preguntamos por una fruta para ver si está en el inventario
fruta_buscada = input("¿Qué fruta te gustaría buscar en el inventario? ")

# Comprobar si la clave existe
if fruta_buscada in inventario_de_frutas:
    print(f"Sí, {fruta_buscada} está en el inventario.")
else:
    print(f"No, {fruta_buscada} no está en el inventario.")

# Definición del diccionario: Usamos el mismo diccionario que hemos estado usando, 
# que contiene detalles de diferentes frutas.

# Interacción con el usuario: Se le pide que ingrese el nombre de una fruta para buscarla en el inventario. 
# Esto hace que el aprendizaje sea más interactivo y 
# les enseña cómo los programas pueden responder a la entrada del usuario.

# Verificar la existencia de una clave: Usamos la sintaxis clave in diccionario 
# para comprobar si la fruta ingresada por el usuario está en el diccionario. 
# Dependiendo del resultado, se imprime un mensaje que confirma o niega la presencia de la fruta en el inventario.