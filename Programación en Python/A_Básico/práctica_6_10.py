# vamos a unir cadenas de caracteres...
cadena1 = ' Calle Malvinas Argentinas 1722'
cadena2 = ' - Barrio Los Alerces'
cadena3 = ' - Manza A Casa 22'
cadena4 = ' - Luján - Mendoza '
cadena5 = ' - Mendoza '

print(cadena1)
print(cadena2)
print(cadena3)
print(cadena4)
print(cadena5)

# cuando concatenamos cadenas usamos el signo +
cadena_concatenada = cadena1 + cadena2 + cadena3 + cadena4 + cadena5
# imprimo
print(cadena_concatenada)

# no podemos concatenar un número con una cadena..
# esto genera un error: print(cadena1 + 100)
#print(cadena1 + 100)

# para poder concatenar un número a una cadena,
# primero lo tenemos que convertir al número en cadena
número = 100
número_a_cadena = str(número)
print(cadena1 + número_a_cadena)