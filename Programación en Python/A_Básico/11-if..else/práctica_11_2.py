# Vamos a suponer que estas son las edades de tres amigos
edad_juan = 12
edad_ana = 10
edad_luis = 8

# Usando 'and' para verificar si todos los amigos tienen 10 años o más
if edad_juan >= 10 and edad_ana >= 10 and edad_luis >= 10:
    print("Todos los amigos tienen 10 años o más.")
else:
    print("Al menos uno de los amigos tiene menos de 10 años.")

# Usando 'or' para verificar si alguno de los amigos tiene exactamente 10 años
if edad_juan == 10 or edad_ana == 10 or edad_luis == 10:
    print("Al menos uno de los amigos tiene exactamente 10 años.")
else:
    print("Ninguno de los amigos tiene 10 años.")

# Usando 'not' para verificar si no es cierto que todos los amigos tienen menos de 10 años
if not (edad_juan < 10 and edad_ana < 10 and edad_luis < 10):
    print("No es cierto que todos los amigos tengan menos de 10 años.")
else:
    print("Todos los amigos tienen menos de 10 años.")

# Definición de variables: Definimos las edades de Juan, Ana y Luis. Esto nos da una base para nuestras comparaciones.

# Operador and:

# Usamos and para asegurarnos de que todas las condiciones se cumplan simultáneamente.
# En este caso, el código verifica si Juan, Ana y Luis tienen 10 años o más. 
# Solo si todos cumplen esta condición, se mostrará el mensaje que todos son mayores o iguales a 10 años.
# Si aunque sea uno no cumple la condición, se ejecutará el bloque de else.

# Operador or:

# Usamos or para verificar si alguna de las condiciones se cumple.
# Aquí, el código comprueba si alguno entre Juan, Ana o Luis tiene exactamente 10 años. 
# Si al menos uno tiene 10 años, se mostrará el mensaje correspondiente.
# Si ninguno tiene 10 años, entonces se muestra el mensaje del bloque de else.

# Aquí utilizamos not para invertir el resultado de la condición que está entre paréntesis.
# El código verifica si todos los amigos tienen menos de 10 años. El operador not invierte esta condición.
# Si es falso que todos tengan menos de 10 años (es decir, al menos uno tiene 10 años o más), 
# entonces se ejecutará el primer bloque de if y se imprimirá el mensaje correspondiente.
# Si todos tienen menos de 10 años, entonces se ejecutará el bloque de else.