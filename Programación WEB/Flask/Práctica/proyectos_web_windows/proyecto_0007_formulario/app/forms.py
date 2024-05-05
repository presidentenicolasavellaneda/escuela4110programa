from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired, Regexp

class PersonForm(FlaskForm):
    name = StringField('Nombre', validators=[
        DataRequired(), 
        Regexp(r'^[a-zA-Z\s]*$', message="El nombre solo debe contener letras.")
    ])
    surname = StringField('Apellido', validators=[
        DataRequired(), 
        Regexp(r'^[a-zA-Z\s]*$', message="El apellido solo debe contener letras.")
    ])
    dni = IntegerField('DNI', validators=[DataRequired()])
    gender = SelectField('Sexo', choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N/S/NC' , 'No Sabe, No contesta')])