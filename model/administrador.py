from model.empleado import Empleado

class Administrador(Empleado):
    # POLIMORFISMO: El admin sobrescribe el método para tener más permisos
    def obtener_permisos(self):
        return ["ver_productos", "agregar_producto", "modificar_producto", "eliminar_producto", "gestionar_empleados"]