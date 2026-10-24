from model.producto_dao import ProductoDAO


class ProductoController:
    def __init__(self):
        self.dao = ProductoDAO()

    def obtener_productos(self):
        return self.dao.listar()

    def guardar_producto(self, nombre, numero, descripcion, cantidad, estado):
        # Validaciones básicas de negocio
        if not nombre or not numero or not descripcion or not cantidad:
            return False, "Todos los campos son obligatorios."

        try:
            cant_int = int(cantidad)
            if cant_int < 0:
                return False, "La cantidad no puede ser negativa."
        except ValueError:
            return False, "La cantidad debe ser un número entero."

        exito = self.dao.crear(nombre, numero, descripcion, cant_int, estado)
        if exito:
            return True, "Producto registrado correctamente."
        return False, "Error al conectar con la base de datos."

    def actualizar_producto(self, id_prod, nombre, numero, descripcion, cantidad, estado):
        if not nombre or not numero or not descripcion or not cantidad:
            return False, "Todos los campos son obligatorios."

        try:
            cant_int = int(cantidad)
            if cant_int < 0:
                return False, "La cantidad no puede ser negativa."
        except ValueError:
            return False, "La cantidad debe ser un número entero."

        exito = self.dao.actualizar(id_prod, nombre, numero, descripcion, cant_int, estado)
        if exito:
            return True, "Producto modificado correctamente."
        return False, "Error al modificar en la base de datos."

    def eliminar_producto(self, id_prod):
        exito = self.dao.eliminar(id_prod)
        if exito:
            return True, "Producto eliminado correctamente."
        return False, "Error al eliminar de la base de datos."