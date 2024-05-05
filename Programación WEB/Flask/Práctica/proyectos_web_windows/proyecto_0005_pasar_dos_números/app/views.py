import json
import os
from datetime import datetime
from flask import render_template, request, redirect, url_for
from .forms import NúmeroFormulario
from app import app

def init_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def form():
        form = NúmeroFormulario(request.form)
        if request.method == 'POST' and form.validate():
                        
            # Datos a mostrar
            data = {
                'número_1': form.número_1.data,
                'número_2': form.número_2.data,
            }
            return redirect(url_for('result', número_1=form.número_1.data , número_2=form.número_2.data))
        return render_template('form.html', form=form)

    @app.route('/result')
    def result():
        número_1 = int(request.args.get('número_1', 0))
        número_2 = int(request.args.get('número_2', 0))
        suma = número_1 + número_2
        data = {
            'número_1': número_1,
            'número_2': número_2,
            'suma': suma
        }
        return render_template('result.html', data=data)