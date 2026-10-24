class Producto:
    def __init__(self, id, nombre, numero, descripcion, cantidad, estado):
        self._id = id
        self._nombre = nombre
        self._numero = numero
        self._descripcion = descripcion
        self._cantidad = cantidad
        self._estado = estado
        
    # Getters
    @property
    def id(self): return self._id
    @property
    def nombre(self): return self._nombre
    @property
    def numero(self): return self._numero
    @property
    def descripcion(self): return self._descripcion
    @property
    def cantidad(self): return self._cantidad
    @property
    def estado(self): return self._estado