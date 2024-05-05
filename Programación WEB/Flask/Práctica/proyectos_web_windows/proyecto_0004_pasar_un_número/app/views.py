"""
Este archivo define las rutas y controladores de la aplicación. 
Maneja las solicitudes GET y POST en la ruta raíz y muestra el resultado en otra página.
"""

from flask import render_template, request, redirect, url_for  # Importa funciones de Flask
from .forms import NúmeroFormulario  # Importa la clase del formulario
from app import app  # Importa la instancia de la aplicación Flask

def init_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def form():
        form = NúmeroFormulario(request.form)  # Crea una instancia del formulario
        if request.method == 'POST' and form.validate():  # Si el formulario es enviado y es válido
            data = {'número': form.número.data}  # Recoge el dato del formulario
            return redirect(url_for('result', número=form.número.data))  # Redirige a la página de resultado
        return render_template('form.html', form=form)  # Renderiza el formulario

    @app.route('/result')
    def result():
        data = {'número': request.args.get('número')}  # Recoge el número desde los argumentos de la URL
        return render_template('result.html', data=data)  # Renderiza la página de resultados con el número