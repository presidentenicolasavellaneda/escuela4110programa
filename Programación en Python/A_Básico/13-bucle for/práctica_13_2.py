# Lista de frutas
frutas = ["manzana", "banana", "cereza", "durazno"]

# Bucle for para recorrer la lista de frutas
for fruta in frutas:
    print("Revisando:", fruta)
    if fruta == "cereza":
        print("¡Cereza encontrada! Terminamos la búsqueda.")
        break  # Termina el bucle

print("Fin del bucle.")

# Lista de Frutas: 
# Tenemos una lista llamada frutas que incluye varios nombres de frutas.
# Bucle For: 
# Empezamos a recorrer la lista con un bucle for. En cada iteración, 
# la variable fruta toma el nombre de la fruta actual de la lista.
# Condicional If: 
# Dentro del bucle, hay una instrucción if que verifica si la fruta actual es "cereza".
# Break: 
# Si encontramos "cereza", imprimimos un mensaje 
# indicando que la hemos encontrado y usamos break para salir del bucle inmediatamente.
# Mensaje Final: Después del bucle, imprimimos "Fin del bucle." para indicar que el bucle ha terminado, 
# ya sea naturalmente o debido al break.