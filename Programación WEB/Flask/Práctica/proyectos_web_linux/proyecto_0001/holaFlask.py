from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, bienvenido a mi aplicación Flask!"

if __name__ == '__main__':
    app.run(debug=True)
