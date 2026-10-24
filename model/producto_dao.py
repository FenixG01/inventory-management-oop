from model.database_connection import DatabaseConnection
from model.producto import Producto

class ProductoDAO:
    def __init__(self):
        self.db = DatabaseConnection()

    def listar(self):
        query = "SELECT id, nam, num, descr, cant, est FROM producto ORDER BY id ASC"
        resultados = self.db.ejecutar_consulta(query)
        productos = []
        if resultados:
            for r in resultados:
                productos.append(Producto(r['id'], r['nam'], r['num'], r['descr'], r['cant'], r['est']))
        return productos

    def crear(self, nombre, numero, descripcion, cantidad, estado):
        query = "INSERT INTO producto (nam, num, descr, cant, est) VALUES (%s,%s,%s,%s,%s)"
        return self.db.ejecutar_accion(query, (nombre, numero, descripcion, cantidad, estado))

    def actualizar(self, id_prod, nombre, numero, descripcion, cantidad, estado):
        query = "UPDATE producto SET nam=%s, num=%s, descr=%s, cant=%s, est=%s WHERE id=%s"
        return self.db.ejecutar_accion(query, (nombre, numero, descripcion, cantidad, estado, id_prod))

    def eliminar(self, id_prod):
        query = "DELETE FROM producto WHERE id=%s"
        return self.db.ejecutar_accion(query, (id_prod,))