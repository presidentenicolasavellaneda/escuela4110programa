"""
Este archivo define los formularios que se usarán en la aplicación. 
NúmeroFormulario es un formulario con un solo campo número que es un campo de entero. 
Este campo requiere un dato (no puede estar vacío), asegurado por el validador DataRequired.
"""

from flask_wtf import FlaskForm  # Importa la clase base FlaskForm para formularios
from wtforms import IntegerField  # Importa IntegerField para usar en los formularios
from wtforms.validators import DataRequired  # Importa el validador DataRequired

class NúmeroFormulario(FlaskForm):
    número = IntegerField('Número', validators=[DataRequired()])
