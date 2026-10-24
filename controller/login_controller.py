from model.database_connection import DatabaseConnection
from model.empleado import Empleado
from model.administrador import Administrador

class LoginController:
    def __init__(self):
        self.db = DatabaseConnection()

    def autenticar(self, usuario, contrasena):
        if not usuario or not contrasena:
            return None, "Los campos no pueden estar vacíos."

        query = "SELECT nom, ape, rfc, rol FROM EMPLOYEE WHERE acces = %s AND rfc = %s"
        res = self.db.ejecutar_consulta(query, (usuario, contrasena))

        if res and len(res) > 0:
            datos = res[0]
            # POLIMORFISMO: Instanciamos la clase hija correcta según el rol
            if datos['rol'] == "Administrador":
                user_obj = Administrador(datos['nom'], datos['ape'], datos['rfc'], usuario, datos['rol'])
            else:
                user_obj = Empleado(datos['nom'], datos['ape'], datos['rfc'], usuario, datos['rol'])
            
            return user_obj, "Éxito"
        else:
            return None, "Usuario o contraseña incorrectos."