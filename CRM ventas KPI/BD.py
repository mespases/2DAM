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
        """ Crea y guarda una factura en la base de datos """
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
        """ Suma la cantidad vendida al producto para poder tener
            informacion sobre el """
        consulta = "UPDATE Producto SET Cantidad_vendida_diaria = Cantidad_vendida_diaria+{0}, Cantidad_vendida_mensual = Cantidad_vendida_mensual+{0}, " \
                   "Cantidad_vendida_trimestral = Cantidad_vendida_trimestral+{0}, Cantidad_vendida_anual = Cantidad_vendida_anual+{0} WHERE Nombre = '{1}';".format(cantidad, producto)

        self.sql.execute(consulta)
        self.sql.commit()

    def resetearCantVendida(self, tipo):
        """ Resetea la cantidad vendida cuando se pasa de dia, mes o anyo"""
        consulta = "UPDATE Producto SET Cantidad_vendida_{0} = 0 WHERE Cantidad_vendida_{0} > 0;".format(tipo)
        self.sql.execute(consulta)
        self.sql.commit()

    def getPrecio(self, producto):
        """ Obtiene el precio del producto pasado por parametro """
        consulta = "SELECT Precio FROM Producto WHERE Nombre = '{}';".format(producto)
        result = self.sql.execute(consulta)

        precio = "no existe este producto"
        for i in result:
            precio = i[0]

        print("El precio de {} es de {}").format(producto, precio)

    def getMediaNumArticulos(self):
        """ Obtiene la media de todos los productos comprados"""
        consulta = "SELECT avg(Num_articulos_comprados) FROM Factura;"
        result = self.sql.execute(consulta)

        media = 0
        for i in result:
            media = i[0]

        print("La media de los articulos vendidos es de: {}").format(media)

    def getTotalIngresos(self):
        """ Obtiene todos los ingresos de la tienda"""
        consulta = "SELECT sum(Total) FROM Factura;"
        result = self.sql.execute(consulta)

        ingresos = 0
        for i in result:
            ingresos = i[0]

        print("El total de los ingresos de la tienda es de: {}").format(ingresos)

    def getProductosMasVendidos(self, tipo):
        """ Obtiene los 5 productos mas vendidos en la tienda"""
        consulta = "SELECT Nombre, Cantidad_vendida_{} FROM Producto;".format(tipo)
        result = self.sql.execute(consulta)

        order = []

        for i in result:
            order.append(i)

        order = sorted(order, key=lambda x: x[1], reverse=True)

        cont = 0
        print("\nLos productos mas vendidos son: ")
        for i in order:
            if cont < 5:
                print("{}: {}").format(i[0], i[1])

            cont += 1

    def getProductosMenosVendidos(self, tipo):
        """ Obtiene los 5 productos menos vendidos en la tienda """
        consulta = "SELECT Nombre, Cantidad_vendida_{} FROM Producto;".format(tipo)
        result = self.sql.execute(consulta)

        order = []

        for i in result:
            order.append(i)

        order = sorted(order, key=lambda x: x[1])

        cont = 0
        print("\nLos productos mas vendidos son: ")
        for i in order:
            if cont < 5:
                print("{}: {}").format(i[0], i[1])

            cont += 1
