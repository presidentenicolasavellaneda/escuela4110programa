"""
Este archivo inicializa la aplicación Flask y establece una clave secreta necesaria para las operaciones de sesión 
y formularios seguros. 
Además, importa las rutas de la aplicación desde el módulo views.
"""
from flask import Flask  # Importa Flask para crear la instancia de la aplicación

app = Flask(__name__)  # Crea una instancia de la aplicación Flask
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'  # Configura una clave secreta para la aplicación (importante para las sesiones y formularios)

from .views import init_routes  # Importa la función init_routes desde el módulo views
init_routes(app)  # Inicializa las rutas de la aplicación con la función importada
