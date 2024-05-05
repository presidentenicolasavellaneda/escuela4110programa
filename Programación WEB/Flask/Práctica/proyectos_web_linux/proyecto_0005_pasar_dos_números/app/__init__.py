from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'

from .views import init_routes
init_routes(app)



