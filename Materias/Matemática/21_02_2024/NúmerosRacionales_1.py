# Números racionales: expresión decimal,comparación

from fractions import Fraction

# Crear dos fracciones
frac1 = Fraction(1, 4)
frac2 = Fraction(1, 3)

# Convertir a decimal
decimal1 = float(frac1)
decimal2 = float(frac2)

print(f"El decimal de 1/4 es {decimal1}")
print(f"El decimal de 1/3 es {decimal2}")

# Comparación
print("1/4 es menor que 1/3:", frac1 < frac2)
