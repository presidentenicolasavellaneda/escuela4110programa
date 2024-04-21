# Números racionales: expresión decimal,comparación

# Para representar gráficamente fracciones y su equivalente decimal de una forma que sea accesible desde una página web, 
# podemos usar Python junto con algunas bibliotecas como Flask para crear un servidor web sencillo 
# y Matplotlib para generar los gráficos. Aquí te dejo un ejemplo de cómo podrías implementarlo:

# Paso 1: Instala las librerías necesarias
# Asegúrate de tener Flask y Matplotlib instalados en tu entorno Python. 
# Puedes instalarlos usando pip:

# pip install flask matplotlib

# Paso 2: Crea el servidor web con Flask
# Vamos a crear un servidor web sencillo que acepte la entrada de una fracción 
# a través de un formulario web, genere un gráfico con Matplotlib mostrando la fracción 
# y su equivalente decimal, y luego devuelva este gráfico como una imagen en la página web.

from flask import Flask, render_template, request, send_file
from fractions import Fraction
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            numerador = int(request.form['numerador'])
            denominador = int(request.form['denominador'])
            if denominador == 0:
                return "El denominador no puede ser cero.", 400
            fraccion = Fraction(numerador, denominador)
            decimal = float(fraccion)
            # Generar gráfico
            fig, ax = plt.subplots()
            categories = ['Fracción', 'Decimal']
            values = [fraccion.numerator / fraccion.denominator, decimal]
            ax.bar(categories, values, color=['blue', 'green'])
            ax.set_ylabel('Valor')
            ax.set_title('Representación de Fracción y Decimal')
            # Guardar gráfico en un buffer
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            return send_file(buf, mimetype='image/png')
        except ValueError:
            return "Por favor, ingrese solo números enteros.", 400
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

# Paso 3: Crea un archivo HTML para el formulario
# Necesitas un archivo HTML simple para enviar los datos del usuario al servidor. 
# Crea un archivo llamado templates/index.html en el mismo directorio que tu script Python:

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Convertidor de Fracciones a Decimales</title>
</head>
<body>
    <h1>Convertidor de Fracciones a Decimales</h1>
    <form method="post">
        Numerador: <input type="text" name="numerador"><br>
        Denominador: <input type="text" name="denominador"><br>
        <input type="submit" value="Convertir y Mostrar Gráfico">
    </form>
</body>
</html>

"""

# Explicación del código:
# El servidor Flask maneja dos rutas: una para mostrar el formulario (GET) y otra para procesar el formulario 
# y mostrar el gráfico (POST).
# Cuando se envía el formulario, el servidor intenta convertir la entrada a números enteros y calcular el decimal 
# de la fracción. Luego, genera un gráfico de barras utilizando Matplotlib, lo guarda en un buffer en memoria, 
# y lo envía como una respuesta de imagen al cliente.
# Si ocurre un error (por ejemplo, si el denominador es cero o si se ingresan caracteres no numéricos), 
# el servidor devuelve un mensaje de error.




