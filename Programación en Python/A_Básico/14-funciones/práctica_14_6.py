# Concepto: Una función es como una receta que nos dice cómo hacer algo paso a paso. 
# Cada vez que queremos hacer eso, 
# simplemente seguimos la receta.

# Vamos a crear una función que pueda recibir una lista de frutas y las imprima una por una. 
# Para hacer esto más interesante y flexible, usaremos *args, 
# así que podrás pasar todas las frutas que quieras como argumentos separados, 
# y la función las manejará como una lista.

def imprimir_frutas(*frutas):
    print("¡Vamos a imprimir la lista de frutas!")
    for fruta in frutas:
        print(fruta)

# Llamada a la función con varias frutas
imprimir_frutas('manzana', 'banano', 'cereza', 'naranja', 'pera')

# Imagina que tienes una caja con futas. 
# Puedes ir sacando una por una y decir su nombe. Esto es lo que hace nuestra función imprimir_frutas: 
# toma cada fruta que le das y la "saca de la caja" para mostrarla.

# En el ejemplo, cuando llamamos a imprimir_frutas('manzana', 'banano', 'cereza', 'naranja', 'pera'), 
# estamos diciendo: "Aquí están las frutas que tengo. ¿Puedes mostrármelas?" Y la función las imprime una por una.