# Concepto: Una función es como una receta que nos dice cómo hacer algo paso a paso. 
# Cada vez que queremos hacer eso, 
# simplemente seguimos la receta.

# Podemos hacer que nuestras funciones sean un poco más inteligentes, 
# haciendo cosas diferentes según lo que necesitemos.

def es_mayor_que_cinco(numero):
    # Esta función verifica si un número es mayor que cinco y devuelve True (Verdadero) si lo es, 
    # y False (Falso) si no lo es.
    if numero > 5:
        return True
    else:
        return False


resultado = es_mayor_que_cinco(6)
print("¿El número 6 es mayor que cinco?:", resultado)  # Esto imprimirá: ¿El número 6 es mayor que cinco?: True