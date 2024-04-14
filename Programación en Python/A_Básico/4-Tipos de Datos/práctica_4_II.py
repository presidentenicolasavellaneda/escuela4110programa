# python tiene funciones para saber los tipos de datos !!!
# para saber qué tipo de datos tiene una variable, uso la función
# type()

# tipo string o tipo cadena
# por ejemplo para un domicilio
calle = 'Malvinas Argentinas'
departamento = 'San Martín'
localidad = 'Palmira'

print('----------------- tipos de datos (algunos)....................')
# si quiero saber los tipos de datos de las variables anteriores
print('...el tipo de dato de la variable calle es : ' , type(calle))
print('...el tipo de dato de la variable departamento es : ' , type(departamento))
print('...el tipo de dato de la variable localidad es : ' , type(localidad))
print('-'*100)

# otro ejemplo, la patente de un auto
patenteAutoVieja = 'AXZ 794'
# la patente de otro auto
patenteAutoNueva = 'AB 123 CD'

print('...el tipo de dato de la variable patenteAutoVieja es : ' , type(patenteAutoVieja))
print('...el tipo de dato de la variable patenteAutoNueva es : ' , type(patenteAutoNueva))
print('-'*100)

# tipos número entero
número = 1378
dni = 40877643
característica = 261
teléfonoFijo = 4452637

print('...el tipo de dato de la variable número es : ' , type(número))
print('-'*100)

# una lista de jugadores de fútbol
miEquipoDeFútbolIdeal = [
    'Lev Yasin',
    'Cafú',
    'Paolo Maldini',
    'Franz Beckenbauer',
    'Roberto Carlos',
    'Zinedine Zidane',
    'Xavi',
    'Maradona',
    'Cristiano Ronaldo',
    'Pelé',
    'Messi'
]

print('...el tipo de dato de la variable miEquipoDeFútbolIdeal es : ' , type(miEquipoDeFútbolIdeal))
print('-'*100)

# una lista de cosas para comprar en el super..
# ojo no se le dice lista, este tipo de datos se llama
# diccionario de datos....
lasComprasDelSuper = {
    'pan' : 2,
    'chocolates' : 10,
    'caramelos' : 40,
    'azucar' : 2,
    'harina' : 5,
    'dulce de leche' : 3,
    'galletas' : 8,
    'jabón' : 4,
    'asado' : 10 
}

print('...el tipo de dato de la variable lasComprasDelSuper es : ' , type(lasComprasDelSuper))
print('-'*100)

# la temperatura ambiente
temperaturaSanMartín = 9.3
temperaturaJunín = 8.7

# la longitud de una calle expresada en metros
longitudCalle = 20.5

# la relación entre la longitud de una circunferencia y su diámetro 
PI = 3.141592

print('...el tipo de dato de la variable temperaturaSanMartín es : ' , type(temperaturaSanMartín))
print('-'*100)


# para expresar si algo es verdadero o falso
variable1 = True
variable2 = False

print('...el tipo de dato de la variable variable1 es : ' , type(variable1))
print('-'*100)

if type(calle) == type(departamento) :
    print('ambas variables son del mismo tipo de dato')
else:
    print('no son del mismo tipo de datos las dos varaibles')