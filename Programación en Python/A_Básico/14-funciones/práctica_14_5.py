# Concepto: Una función es como una receta que nos dice cómo hacer algo paso a paso. 
# Cada vez que queremos hacer eso, 
# simplemente seguimos la receta.

# vamos a hablar sobre algo en Python que se llama *args, que es una forma corta de decir "argumentos". 
# Esto puede sonar complicado, pero es como tener una caja mágica donde puedes poner todas las cosas que quieras, 
# ¡sin saber cuántas cosas son desde el principio!

# Imagina que tienes una mochila que puedes llenar con todos los juguetes que quieras llevar al parque. 
# Algunos días tal vez quieras llevar solo un yo-yo y un frisbee, 
# pero otros días podrías querer llevar un balón, una cuerda para saltar, 
# un camión de juguete, y mucho más. *args es como esa mochila: 
# puedes poner dentro tantas cosas como quieras cuando usas una función en Python.

# Vamos a hacer una función que se llama sumar_numeros, que sumará todos los números que le demos, 
# sin importar cuántos sean.

# En este ejemplo, *args actúa como una lista de todos los números que pasamos a la función. 
# La función luego los suma todos.

def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

print("La suma de 3, 5 y 10 es:", sumar_numeros(3, 5, 10))  # Esto imprimirá: La suma de 3, 5 y 10 es: 18
print("La suma de 4 y 2 es:", sumar_numeros(4, 2))  # Esto imprimirá: La suma de 4 y 2 es: 6

# ¿Cómo funciona *args?
# Cuando escribes *args en la definición de una función, 
# le estás diciendo a Python: 
# "Puedo recibir cualquier cantidad de argumentos en esta función, y quiero que los trates como una lista."

# Puedes pensar en *args como un truco para hacer tus funciones más flexibles y divertidas 
# porque no tienes que preocuparte por el número exacto de cosas que vas a recibir. 
# Es como si tuvieras una fiesta y dijeras, "¡Todos están invitados!" y no importa cuántos amigos vengan.