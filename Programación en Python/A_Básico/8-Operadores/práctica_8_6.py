# precedencia de operadores
# La precedencia de operadores determina el orden en que se realizan las operaciones en una expresión.

# Ejemplo de una expresión matemática simple
resultado = 10 + 2 * 5
print('El resultado de 10 + 2 * 5 es:', resultado)  # Esto imprimirá: 20

# ¿Por qué? Porque la multiplicación tiene mayor precedencia que la suma, entonces se realiza primero:
# 1. Primero se multiplica 2 * 5 = 10
# 2. Luego se suma 10 + 10 = 20

# Usando paréntesis para cambiar la precedencia
resultado_con_parentesis = (10 + 2) * 5
print('El resultado de (10 + 2) * 5 es:', resultado_con_parentesis)  # Esto imprimirá: 60

# En este caso, los paréntesis cambian la precedencia, haciendo que la suma se realice antes de la multiplicación:
# 1. Primero se suma 10 + 2 = 12
# 2. Luego se multiplica 12 * 5 = 60


# Sin paréntesis: En la primera expresión, Python sigue las reglas de precedencia estándar 
# donde la multiplicación (*) tiene mayor prioridad que la suma (+). 
# Por eso, multiplica 2 * 5 antes de sumarlo a 10.

# Con paréntesis: En la segunda expresión, los paréntesis cambian la precedencia normal, 
# haciendo que la operación dentro de los paréntesis (la suma) se realice antes de la multiplicación. 
# Los paréntesis tienen la mayor precedencia en Python y en la mayoría de los lenguajes de programación.