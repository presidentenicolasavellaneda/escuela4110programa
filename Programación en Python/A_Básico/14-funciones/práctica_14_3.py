# Concepto: Una función es como una receta que nos dice cómo hacer algo paso a paso. 
# Cada vez que queremos hacer eso, 
# simplemente seguimos la receta.

# A veces queremos que nuestra función nos dé algo de vuelta, 
# como cuando preguntas cuánto es 2 + 3 
# y esperas que te digan 5.

def sumar_dos_numeros(a, b):
    resultado = a + b
    return resultado

# En este caso, sumar_dos_numeros toma dos números, 
# los suma y luego return nos da el resultado de vuelta.

suma = sumar_dos_numeros(3, 5)
print("El resultado de sumar 3 y 5 es:", suma)  # Esto imprimirá: El resultado de sumar 3 y 5 es: 8