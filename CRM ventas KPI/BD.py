import sqlite3

class BD:

    # Conexion sql
    sql = sqlite3.connect("kpi.db", timeout=10)
    cursor = sql.cursor()

    productos = []

    def selectProductos(self):
        """ Muestra por pantalla la lista de los productos """
        consulta = "SELECT Nombre FROM Producto;"
        result = self.sql.execute(consulta)

        print("\nLista de productos: ")
        for producto in result:
            print(producto[0])
            self.productos.append(producto[0])

    def crearFacturaBD(self, producto, cantidad, nombre):
        consulta = "SELECT Precio FROM Producto WHERE Nombre = '{}';".format(producto)
        result = self.sql.execute(consulta)

        for i in result:
            precio = i[0]

        total = precio*cantidad
        insert = "INSERT INTO Factura (Nombre_cliente, Total, Num_articulos_comprados) VALUES ('{}', {}, {});".format(nombre, total, cantidad)
        self.sql.execute(insert)
        self.sql.commit()

        return total

    def sumarCantidades(self, producto, cantidad):
        consulta = "UPDATE Producto SET Cantidad_vendida_diaria = Cantidad_vendida_diaria+{0}, Cantidad_vendida_mensual = Cantidad_vendida_mensual+{0}, " \
                   "Cantidad_vendida_trimestral = Cantidad_vendida_trimestral+{0}, Cantidad_vendida_anual = Cantidad_vendida_anual+{0} WHERE Nombre = '{1}';".format(cantidad, producto)
        self.sql.execute(consulta)
        self.sql.commit()

