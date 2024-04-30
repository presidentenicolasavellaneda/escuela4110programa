# Concepto: Una función es como una receta que nos dice cómo hacer algo paso a paso. 
# Cada vez que queremos hacer eso, 
# simplemente seguimos la receta.

# Una función recursiva es una función que se llama a sí misma para resolver un problema. 
# Es como si estuvieras resolviendo un gran rompecabezas y para colocar cada pieza, 
# tuvieras que resolver un rompecabezas más pequeño dentro de él.

# Vamos a hacer un ejemplo sencillo y divertido: 
# vamos a calcular el factorial de un número utilizando una función recursiva. 
# El factorial de un número es el producto de todos los números enteros positivos 
# desde 1 hasta ese número. Por ejemplo, el factorial de 5 (escrito como 5!) es 5 × 4 × 3 × 2 × 1 = 120.
                                                          
def factorial(n):
    # Si el número es 1, no necesitamos multiplicar más, solo devolvemos 1
    if n == 1:
        return 1
    else:
        # Multiplicamos el número por el factorial del número anterior
        return n * factorial(n - 1)

# Llamamos a la función con un número
numero = 5
resultado = factorial(numero)
print("El factorial de", numero, "es", resultado)

# Imagina que tienes una pila de bloques numerados del 1 al 5 y quieres saber cuántas formas diferentes 
# hay de apilarlos todos, sin dejar ninguno afuera y sin repetir ningún número en el orden. 
# Para hacer eso, primero colocas el bloque 5, y luego necesitas apilar los bloques del 1 al 4 
# de todas las maneras posibles. Pero para saber cómo apilar del 1 al 4, 
# necesitas saber cómo apilar del 1 al 3, y así sucesivamente hasta que solo te queda un bloque.

# Así funciona nuestra función factorial: empieza con el número más grande, 
# y luego pregunta "¿cuánto sería si yo tuviera uno menos?" y sigue preguntando eso hasta que solo queda 1. 
# Cada vez que la función se llama a sí misma con un número menor, 
# está como si quitara un bloque de la pila y calculando todas las formas posibles con los bloques restantes.

# Usar funciones recursivas puede hacer que algunos problemas complicados sean más fáciles de entender 
# y resolver porque divides el problema grande en problemas pequeñitos que son más fáciles de manejar. 
# Es como decir "si sé resolver esto para un caso pequeño, puedo usar eso para resolverlo para casos más grandes paso a paso".