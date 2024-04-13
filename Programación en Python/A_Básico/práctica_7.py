# booleans o booleanos
# para representar un valor booleano usamos:
# True o False

# ejemplo

llueve = True
frio = False

print(llueve)
print(frio)

# True significa verdadero, también puedes interpretarlo como 'si o afirmativo'
# False significa falso, también puedes interpretarlo como 'no o negativo

if llueve == True:
    print('Está lloviendo..!!!, mejor salgo con el paraguas')
else:
    print('Si no llueve, no necesito el paraguas')

print('-'*100)

# puedo comparar valores y determinar si uno es más grande que el otro

valor_1 = 300
valor_2 = 200

if valor_1 > valor_2:
    print('el valor 1 es mas grande que el valor_2')
else:
    print('el valor_1 es mas chico que el valor_2')

# puedo comparar dos cadenas de caracteres para ver si son iguales

cadena_1 = 'hola'
cadena_2 = 'hola'

if cadena_1 == cadena_2:
    print('las dos cadenas son iguales')
else:
    print('las dos cadenas son diferentes')

print('-'*100)
