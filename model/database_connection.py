import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

class DatabaseConnection:
    def __init__(self):
        self.config = DB_CONFIG

    def get_connection(self):
        try:
            return mysql.connector.connect(**self.config)
        except Error as e:
            print(f"Error de conexión a MySQL: {e}")
            return None

    def ejecutar_consulta(self, query, params=()):
        conexion = self.get_connection()
        if not conexion:
            return None
        try:
            cursor = conexion.cursor(dictionary=True) # Devuelve diccionarios
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            cursor.close()
            conexion.close()
            return resultados
        except Error as e:
            print(f"Error en consulta: {e}")
            return None

    def ejecutar_accion(self, query, params=()):
        conexion = self.get_connection()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute(query, params)
            conexion.commit()
            cursor.close()
            conexion.close()
            return True
        except Error as e:
            print(f"Error al guardar datos: {e}")
            return False