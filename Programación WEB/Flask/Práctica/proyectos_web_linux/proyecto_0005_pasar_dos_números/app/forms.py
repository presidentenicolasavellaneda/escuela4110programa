from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired, Regexp

class NúmeroFormulario(FlaskForm):    
    número_1 = IntegerField('Número 1', validators=[DataRequired()])
    número_2 = IntegerField('Número 2', validators=[DataRequired()])