# Usar pop() para remover y obtener un elemento de una lista
# Imagina que tienes una lista de frutas y quieres sacar la última fruta de la lista para comerla.

# Lista de frutas
frutas = ['manzana', 'banana', 'cereza', 'naranja', 'kiwi']

# Mostrar la lista original de frutas
print('Lista original de frutas:', frutas)

# Usar pop sin índice para sacar y mostrar la última fruta de la lista
ultima_fruta = frutas.pop()
print('He sacado la fruta:', ultima_fruta)
print('Lista de frutas después de sacar la última:', frutas)

# Ahora, si quieres sacar una fruta específica, como la primera fruta (índice 0)
primera_fruta = frutas.pop(0)
print('He sacado la primera fruta:', primera_fruta)
print('Lista de frutas después de sacar la primera:', frutas)

# Lista de frutas: Empezamos con una lista de frutas. Es importante mostrar la lista original

# Remover la última fruta: Al usar pop() sin especificar un índice, 
# se remueve y devuelve la última fruta de la lista. 
# Esto es útil para entender cómo se puede manipular listas cuando se quiere trabajar con el último elemento.

# Remover una fruta específica: También se puede usar pop() con un índice específico 
# para sacar un elemento en particular. 
# En este caso, removemos la primera fruta (índice 0). 
# Esto enseña cómo los índices pueden controlar qué elementos se remueven.
