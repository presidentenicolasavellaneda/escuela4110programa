# Números racionales: expresión decimal,comparación

from fractions import Fraction

def obtener_entrada_usuario():
    while True:
        try:
            # Solicita al usuario que ingrese el numerador
            numerador = int(input("Ingrese el numerador: "))
            # Solicita al usuario que ingrese el denominador
            denominador = int(input("Ingrese el denominador (diferente de cero): "))
            if denominador == 0:
                print("El denominador no puede ser cero. Por favor, intente de nuevo.")
                continue
            return numerador, denominador
        except ValueError:
            print("Por favor, ingrese solo números enteros. Intente de nuevo.")

def main():
    print("Bienvenido al conversor de fracciones a decimales.")
    numerador, denominador = obtener_entrada_usuario()
    fraccion = Fraction(numerador, denominador)
    decimal = float(fraccion)
    print(f"La fracción {fraccion} es equivalente al decimal {decimal}.")

if __name__ == "__main__":
    main()

