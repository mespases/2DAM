import sqlite3

class BD:

    # Conexion mysql
    mysql = sqlite3.connect("C:\Users\miguel.espases\Desktop\TestGit\Clase\Tienda.db", timeout=10)
    cursor = mysql.cursor()

    def insert_personal(self, nombre, edad):
        consulta = "INSERT INTO Personal (nombre, edad) VALUES ('{}', {});".format(nombre, edad)
        self.mysql.execute(consulta)
        self.mysql.commit()
        print("El usuario se ha insertado correctamente")

    def select_personal(self):
        consulta = "SELECT * FROM Personal;"
        resultado = self.mysql.execute(consulta)

        for result in resultado:
            print(result)

    def update_productos(self, cantidad, nombre_producto):
        lista = ['Sal', 'Azucar', 'Agua']
        if cantidad >= 0 and nombre_producto in lista:
            consulta = "UPDATE Productos SET cantidad = {} + {} WHERE nombre = '{}';".format(cantidad, cantidad, nombre_producto)
            self.mysql.execute(consulta)
            self.mysql.commit()
            print("Se ha realizado el pedido del producto")

        else:
            print("La cantidad o el producto introducido son erroneos")

    def select_productos(self):
        consulta = "SELECT * FROM Productos;"
        resultado = self.mysql.execute(consulta)

        for result in resultado:
            print(result)

    def update_ganancias_mas_1(self, nombre_tienda):
        consulta1 = "UPDATE Ganancias SET cantidad_vendida = cantidad_vendida + 1 WHERE tienda = '{}';".format(nombre_tienda)
        consulta2 = "UPDATE Ganancias SET dinero_ganado = dinero_ganado + 1 WHERE tienda = '{}';".format(nombre_tienda)
        self.mysql.execute(consulta1)
        self.mysql.execute(consulta2)
        self.mysql.commit()

    def select_ganancias(self):
        consulta = "SELECT * FROM Ganancias;"
        resultado = self.mysql.execute(consulta)

        for result in resultado:
            print(result)

    def close_mysql(self):
        self.mysql.close()