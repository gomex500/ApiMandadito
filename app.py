from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.settings import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Conexión segura configurada"

# @app.route('/')
# def hola_mundo():
#     return '¡Hola Mundo desde Flask!'




if __name__ == '__main__':
    app.run(debug=True)
