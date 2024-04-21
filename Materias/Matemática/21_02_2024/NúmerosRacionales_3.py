# Números racionales: expresión decimal,comparación
# pip install tkintertable
# ubuntu: sudo apt-get install python3-tk
# sudo apt install python3.9-tk
# sudo apt install python3.10-tk

import tkinter as tk
from tkinter import simpledialog, messagebox
from fractions import Fraction
import matplotlib.pyplot as plt

def ask_for_integer(prompt):
    """
    Solicita al usuario un número entero, asegurándose de que la entrada sea válida.
    Si la entrada no es un número entero, muestra un mensaje de error y vuelve a solicitarlo.
    Si el usuario cierra la ventana, devuelve None.
    """
    root = tk.Tk()
    root.withdraw()  # Esconder la ventana principal de tkinter
    while True:
        try:
            value = simpledialog.askstring("Input", prompt, parent=root)
            if value is None:  # Si el usuario cierra la ventana
                return None
            value = int(value)  # Intenta convertir la entrada a un entero
            return value
        except ValueError:  # Manejar el error si la conversión falla
            messagebox.showerror("Error", "Por favor, ingrese solo números enteros.")

def show_fraction():
    """
    Solicita al usuario el numerador y el denominador para formar una fracción.
    Luego, muestra esta fracción y su equivalente decimal en un gráfico de barras.
    """
    numerador = ask_for_integer("Ingrese el numerador:")
    if numerador is None:  # Si el usuario cierra la ventana
        return
    
    denominador = ask_for_integer("Ingrese el denominador:")
    if denominador is None or denominador == 0:  # Si el usuario cierra la ventana o introduce un 0
        messagebox.showerror("Error", "El denominador no puede ser cero.")
        return
    
    # Calcular fracción y decimal
    fraccion = Fraction(numerador, denominador)
    decimal = float(fraccion)
    
    # Crear y mostrar el gráfico
    fig, ax = plt.subplots()
    categories = ['Fracción', 'Decimal']
    values = [fraccion.numerator / fraccion.denominator, decimal]
    bars = ax.bar(categories, values, color=['blue', 'green'])
    
    # Añadir texto debajo de cada barra
    ax.text(bars[0].get_x() + bars[0].get_width() / 2, values[0] * 0.95, str(fraccion),
            ha='center', va='bottom', color='white', fontweight='bold')
    ax.text(bars[1].get_x() + bars[1].get_width() / 2, values[1] * 0.95, f'{decimal:.2f}',
            ha='center', va='bottom', color='white', fontweight='bold')
    
    ax.set_ylabel('Valor')
    ax.set_title('Representación de Fracción y Decimal')
    plt.show()

# Configurar y ejecutar la aplicación principal
if __name__ == "__main__":
    show_fraction()