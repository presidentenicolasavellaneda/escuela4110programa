# Lista de frutas
frutas = ["manzana", "banana", "cereza", "durazno"]

# Bucle for para recorrer la lista de frutas
for fruta in frutas:
    if fruta == "banana":
        print("Banana saltada!")
        continue  # Salta el resto del código en esta iteración
    print("Fruta procesada:", fruta)

print("Fin del bucle.")

# Lista de Frutas: 
# Tenemos una lista llamada frutas con varios nombres de frutas.
# Bucle For: 
# Iniciamos un bucle for que recorre la lista de frutas. 
# En cada iteración, la variable fruta toma el nombre de la fruta actual de la lista.
# Condicional If: Dentro del bucle, hay una instrucción if que verifica si la fruta actual es "banana".
# Continue: 
# Si la fruta es "banana", imprimimos "Banana saltada!" 
# y usamos continue para saltar el resto del código en esta iteración y pasar directamente a la siguiente fruta.
# Impresión: Si la fruta no es "banana", imprimimos que la fruta ha sido procesada.
# Mensaje Final: Después del bucle, imprimimos "Fin del bucle." para indicar que hemos terminado de recorrer la lista.