# operadores lógicos
# Los operadores lógicos nos ayudan a combinar condiciones verdaderas o falsas.

# Operador AND (y)
# Para que el resultado sea True, todas las condiciones deben ser True.
# AND (and): Este operador devuelve True solo si todas las condiciones 
#            combinadas con and son verdaderas. En el ejemplo, solo puede comer si tiene hambre y hay comida disponible.
tiene_hambre = True
hay_comida = True
puede_comer = tiene_hambre and hay_comida
print('¿Puede comer?', puede_comer)  # Esto imprimirá: True

# Operador OR (o)
# Para que el resultado sea True, al menos una de las condiciones debe ser True.
# OR (or):   Este operador devuelve True si al menos una de las condiciones es verdadera. 
#            En el ejemplo, puede salir si es fin de semana o si tiene permiso.
es_fin_de_semana = False
tiene_permiso = True
puede_salir = es_fin_de_semana or tiene_permiso
print('¿Puede salir?', puede_salir)  # Esto imprimirá: True

# Operador NOT (no)
# Invierte el resultado de la condición: True se convierte en False, y viceversa.
# NOT (not): Este operador invierte el resultado de la condición; si es True, devuelve False, 
#            y si es False, devuelve True. En el ejemplo, cambia el día de escuela a no ser día de escuela.
es_dia_de_escuela = True
no_es_dia_de_escuela = not es_dia_de_escuela
print('¿No es día de escuela?', no_es_dia_de_escuela)  # Esto imprimirá: False