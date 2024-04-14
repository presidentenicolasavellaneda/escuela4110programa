# los strings como arreglos o arrays (arrays es un tipo de variable especial)
# vamos a recortar una parte de la cadena de texto

dirección = ' Calle Malvinas Argentinas 1722 - Barrio Los Alerces - Manza A Casa 22 - Luján - Mendoza '
inicio = 2
fin = 10 # no se incluye esa posición
recorte = dirección[inicio:fin]
print(recorte)

print('-'*50)

# también podemos recortar desde le incio hasta un punto determinado
print(dirección[:20])
print('-'*50)

# podemos recortar desde un lugar hasta al final
print(dirección[20:])
print('-'*50)