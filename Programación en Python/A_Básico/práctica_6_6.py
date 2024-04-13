# los strings como arreglos o arrays (arrays es un tipo de variable especial)
# vamos a usar una estructrura condicional para saber si una sub cadena
# está presente o no en otra cadena

dirección = '''
Calle Malvinas Argentinas 1722 - 
Barrio Los Alerces -
Manza A Casa 22 -
Luján - Mendoza
'''
print('*'*50 , 'Dirección ' , '*'*50)
print(dirección)
print('*'*100)
palabra_a_buscar = input('buscar en la dirección (puede ser una letra o parte de una palabra): ')
print('*'*100)


# usando un condicional
if palabra_a_buscar in dirección:
    print(f'{palabra_a_buscar} está en la cadena')
else:
    print(f'{palabra_a_buscar} no está dentro de la cadena')

print('..fin..')