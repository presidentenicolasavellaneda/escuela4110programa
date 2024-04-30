# los strings como arreglos o arrays (arrays es un tipo de variable especial)
# vamos a usar una estructrura condicional para saber si una sub cadena
# está presente o no en otra cadena

dirección = '''
Calle Malvinas Argentinas 1722 - 
Barrio Los Alerces -
Manza A Casa 22 -
Luján - Mendoza
'''

if 'Lujáaaan' not in dirección:
    print('Lujáaaan no está en la dirección')