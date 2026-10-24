from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre: str, apellido: str, rfc: str):
        # ENCAPSULACIÓN: Atributos protegidos
        self._nombre = nombre
        self._apellido = apellido
        self._rfc = rfc

    @property
    def nombre_completo(self):
        return f"{self._nombre} {self._apellido}"

    # HERENCIA Y POLIMORFISMO: Método abstracto que las hijas deben sobrescribir
    @abstractmethod
    def obtener_permisos(self):
        pass