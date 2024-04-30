# Nivel actual del jugador y monedas que posee
nivel_del_jugador = 5
monedas_del_jugador = 50

# Nivel necesario para desbloquear una habilidad y costo del artículo especial
nivel_para_habilidad = 10
costo_articulo_especial = 40

# Verificación del nivel del jugador
if nivel_del_jugador >= nivel_para_habilidad:
    print("¡Felicidades! Has desbloqueado una nueva habilidad.")
else:
    print("Aún necesitas alcanzar el nivel 10 para desbloquear la habilidad especial.")
    # Verificación de monedas para comprar un artículo
    if monedas_del_jugador >= costo_articulo_especial:
        print("Sin embargo, tienes suficientes monedas para comprar un artículo especial.")
    else:
        print("Además, no tienes suficientes monedas para comprar el artículo especial.")

# Primer nivel de if:

# Primero, se comprueba si el jugador tiene el nivel suficiente para desbloquear una habilidad 
# (nivel_del_jugador >= nivel_para_habilidad).
# Si la condición es verdadera, se felicita al jugador por desbloquear la habilidad.
# Si la condición es falsa, se le informa que necesita alcanzar un nivel mayor.
# Anidamiento de if dentro del else:

# Dentro del bloque else (que se ejecuta si el jugador no ha alcanzado el nivel necesario), añadimos otro if.
# Este nuevo if comprueba si el jugador tiene suficientes monedas 
# para comprar un artículo especial (monedas_del_jugador >= costo_articulo_especial).
# Si el jugador tiene las monedas, se le informa que puede comprar el artículo.
# Si no, se le dice que tampoco tiene suficientes monedas para comprar el artículo.