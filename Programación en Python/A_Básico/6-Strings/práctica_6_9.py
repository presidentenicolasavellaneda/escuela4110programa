# usando los métodos de las cadenas
# las cadenas de caracteres son objetos...
# los strings como arreglos o arrays (arrays es un tipo de variable especial)
# vamos a recortar modificar la cadena de caracteres

dirección = ' Calle Malvinas Argentinas 1722 - Barrio Los Alerces - Manza A Casa 22 - Luján - Mendoza '

# vamos a hacer que queden todas las letras en myúsculas
print('original   : ' , dirección)
print('mayúsculas : ' , dirección.upper())
print('-'*110)

# ahora vamos a hacer que queden todas en minúsculas
print('original   : ' , dirección)
print('mayúsculas : ' , dirección.lower())
print('-'*110)

# vamos a quitarles el espacio que está adlante 
print('original   : ' , dirección)
print('mayúsculas : ' , dirección.strip())
print('-'*110)

# vamos a quitarles todos los espacios en blanco
print('original   : ' , dirección)
print('mayúsculas : ' , dirección.replace(' ',''))
print('-'*110)

# vamos a cortar una cadena donde tenga espacios en blanco
# me va a devolver una lista con todas las palabras..!!!
# ...esto está buenísimo para poder hacer muchas cosas más..!!
print('original   : ' , dirección)
print('mayúsculas : ' , dirección.split(' '))
print('-'*110)

# hay muchos métodos más para remover los espacios..
# fijate acá : https://www.w3schools.com/python/python_ref_string.asp