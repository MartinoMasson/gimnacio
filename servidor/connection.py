import mysql.connector
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

# Obtener las variables de entorno
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

def Abrir_conexion():
    try:
        # Establecer la conexión con la base de datos
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME 
        )
        return conn
    
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None

def cerrar_conexion(conn, cursor):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    
conn = Abrir_conexion()
if conn:
    cursor = conn.cursor()