y = ' '
for x in "banana":
  print('x :' , x)
  print('y :' , y)
  y =  x + y
print(y)

# Inicializamos y: Al principio, y es un espacio en blanco (' '). 
# Esto significa que y está vacío y listo para que le añadamos cosas.

# El bucle for: La línea for x in "banana": nos dice que vamos a hacer algo con cada letra de la palabra "banana". 
# En cada vuelta del bucle, la variable x tomará una letra de la palabra "banana", empezando por la 'b' y terminando en la última 'a'.

# Imprimir x y y: Dentro del bucle, imprimimos el valor de x 
# (que es la letra actual de "banana" con la que estamos trabajando) y 
# y (que al principio es sólo un espacio en blanco).

# Actualizar y: Luego, actualizamos y para que sea igual a x + y. 
# Esto significa que cada letra que tomamos se añade al frente de lo que ya está en y. Es como si estuviéramos poniendo las letras en una pila, pero al revés.

# Resultado final: Después de que el bucle ha pasado por todas las letras, 
# y se ha construido agregando cada nueva letra al principio. 
# Entonces, al final, y será "ananab", que es "banana" al revés.