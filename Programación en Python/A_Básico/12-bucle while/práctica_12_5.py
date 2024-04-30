import random

# El programa escoge un número al azar entre 1 y 10
numero_secreto = random.randint(1, 10)

# Instrucciones para el jugador
print("He pensado un número entre 1 y 10. ¡Intenta adivinarlo!")

# El jugador empieza a adivinar el número
adivinanza = None

while adivinanza != numero_secreto:
    # El jugador introduce su adivinanza
    adivinanza = int(input("¿Cuál crees que es el número? "))
    
    # Comprobamos si la adivinanza es correcta
    if adivinanza == numero_secreto:
        print("¡Correcto! ¡Has adivinado el número!")
    else:
        print("Eso no es correcto. Intenta de nuevo.")

# Importar random: Usamos import random para poder generar un número al azar.
# Generar el número secreto: numero_secreto = random.randint(1, 10) elige un número al azar entre 1 y 10.
# Inicio del bucle while: while adivinanza != numero_secreto: 
# mantiene el bucle en ejecución mientras que la adivinanza del jugador no sea igual al número secreto.
# Pedir al jugador que adivine: Dentro del bucle, el jugador es invitado a introducir un número usando input(). 
# Convertimos esta entrada a un entero con int().
# Chequeo de la condición: Si el jugador acierta (adivinanza == numero_secreto), 
# se imprime un mensaje de éxito y el bucle termina. Si no acierta, 
# el bucle continúa y se pide al jugador que intente de nuevo.