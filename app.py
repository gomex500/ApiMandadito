from flask import Flask
import pyodbc

app = Flask(__name__)

# @app.route('/')
# def hola_mundo():
#     return '¡Hola Mundo desde Flask!'

# Configura tu conexión a SQL Server
server = 'localhost'  # o IP o nombre del servidor
database = 'PRUEBA'
username = 'sa'
password = 'Freddy@500'
driver = 'ODBC Driver 17 for SQL Server'  # Asegúrate que está instalado

# Cadena de conexión
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

@app.route('/')
def probar_conexion():
    try:
        with pyodbc.connect(conn_str) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT GETDATE()")
            resultado = cursor.fetchone()
            return f'Conexión exitosa. Fecha actual en SQL Server: {resultado[0]}'
    except Exception as e:
        return f'Error en la conexión: {e}'

if __name__ == '__main__':
    app.run(debug=True)
