
print("¡Hola! ¿Cómo te llamas?")

nombre = input()
print("¡Encantado de conocerte, " + nombre + "!")

print("¿Cómo estás, " + nombre + "? (bien/mal)")
estado = input().lower()  # .lower() convierte la entrada a minúsculas

if estado == "bien":
    print("¡Qué bueno que estás bien, " + nombre + "!")
else:
    print("Espero que tu día mejore, " + nombre + ".")