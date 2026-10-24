from model.persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, apellido, rfc, usuario, rol):
        super().__init__(nombre, apellido, rfc)
        self._usuario = usuario
        self._rol = rol

    @property
    def usuario(self): return self._usuario
    
    @property
    def rol(self): return self._rol

    # POLIMORFISMO: Sobrescritura del método abstracto
    def obtener_permisos(self):
        return ["ver_productos"]