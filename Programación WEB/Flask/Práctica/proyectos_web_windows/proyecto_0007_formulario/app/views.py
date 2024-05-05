import json
import os
from datetime import datetime
from flask import render_template, request, redirect, url_for
from .forms import PersonForm
from app import app

def init_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def form():
        form = PersonForm(request.form)
        if request.method == 'POST' and form.validate():
            # Crear el identificador único basado en la fecha y hora
            unique_id = datetime.now().strftime("%Y%m%d%H%M%S")
            
            # Datos a guardar
            data = {
                'id': unique_id,
                'name': form.name.data,
                'surname': form.surname.data,
                'dni': form.dni.data,
                'gender': form.gender.data
            }

            # Ruta del archivo JSON
            file_dir = os.path.join(app.root_path, 'static', 'data')
            os.makedirs(file_dir, exist_ok=True)  # Simplificado para crear directorios necesarios
            file_path = os.path.join(file_dir, 'data.json')
            
            # Leer datos existentes y agregar los nuevos
            if os.path.exists(file_path):
                with open(file_path, 'r') as json_file:
                    try:
                        existing_data = json.load(json_file)
                        if not isinstance(existing_data, list):
                            existing_data = []  # Asegura que los datos existentes sean una lista
                    except json.JSONDecodeError:
                        existing_data = []  # Maneja posibles errores de decodificación
            else:
                existing_data = []

            existing_data.append(data)

            # Escribir datos actualizados de nuevo al archivo JSON
            with open(file_path, 'w') as json_file:
                json.dump(existing_data, json_file)

            return redirect(url_for('result', name=form.name.data, surname=form.surname.data, dni=form.dni.data, gender=form.gender.data))
        return render_template('form.html', form=form)

    @app.route('/result')
    def result():
        data = {
            'name': request.args.get('name'),
            'surname': request.args.get('surname'),
            'dni': request.args.get('dni'),
            'gender': request.args.get('gender')
        }
        return render_template('result.html', data=data)
    
    # Dentro de views.py, añadir esta nueva ruta
    @app.route('/view_all')
    def view_all():
        file_path = os.path.join(app.root_path, 'static', 'data', 'data.json')
        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        return render_template('view_all.html', data=data)

