import os
from dotenv import load_dotenv
import mysql.connector


#ACTIVAR ENTORNO VIRTUAL
# .venv\Scripts\activate  
# Cargar variables de entorno desde el archivo .env
load_dotenv()

conexion = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT"))
)
print("Conexión exitosa a la base de datos")
