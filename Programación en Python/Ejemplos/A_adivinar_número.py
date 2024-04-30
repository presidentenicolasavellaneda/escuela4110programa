import random

numero_secreto = random.randint(1, 10)
intento = None

while intento != numero_secreto:
    intento = int(input("Adivina el número que estoy pensando (entre 1 y 10): "))
    
    if intento < numero_secreto:
        print("Más alto...")
    
    elif intento > numero_secreto:
        print("Más bajo...")

print("¡Felicidades! ¡Has adivinado el número!")