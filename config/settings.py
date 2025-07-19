from decouple import config
import urllib

# Leer variables del .env
DB_SERVER = config('DB_SERVER')
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DRIVER = 'ODBC Driver 17 for SQL Server'

# Codificar la cadena de conexión
params = urllib.parse.quote_plus(
    f"DRIVER={DRIVER};"
    f"SERVER={DB_SERVER};"
    f"DATABASE={DB_NAME};"
    f"UID={DB_USER};"
    f"PWD={DB_PASSWORD}"
)

# URI compatible con SQLAlchemy
SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc:///?odbc_connect={params}"
