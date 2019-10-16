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
        lista = ['Limon', 'Azucar', 'Agua']
        if cantidad >= 0 and nombre_producto in lista:
            consulta = "UPDATE Productos SET cantidad_ml_g = cantidad_ml_g + {} WHERE nombre = '{}';".format(cantidad, nombre_producto)
            self.mysql.execute(consulta)
            self.mysql.commit()
            print("Se ha realizado el pedido del producto")

        else:
            print("La cantidad o el producto introducido son erroneos")

    def producir_productos_1L(self):
        if self.comprobar_productos():
            restar_limonada = "UPDATE Productos SET cantidad_ml_g = cantidad_ml_g - 500 WHERE nombre = 'Limon';"
            restar_azucar = "UPDATE Productos SET cantidad_ml_g = cantidad_ml_g - 100 WHERE nombre = 'Azucar';"
            restar_agua = "UPDATE Productos SET cantidad_ml_g = cantidad_ml_g - 500 WHERE nombre = 'Agua';"
            sumar_limonada = "UPDATE Productos SET cantidad_ml_g = cantidad_ml_g + 1000 WHERE nombre = 'Limonada';"

            self.mysql.execute(restar_limonada)
            self.mysql.execute(restar_azucar)
            self.mysql.execute(restar_agua)
            self.mysql.execute(sumar_limonada)
            self.mysql.commit()
            print("Se ha producido 1L de Limonada")
        else:
            print("No tienes suficientes materiales para craftear limonada")

    def comprobar_productos(self):
        consulta1 = "SELECT cantidad_ml_g FROM Productos WHERE nombre = 'Limon';"
        consulta2 = "SELECT cantidad_ml_g FROM Productos WHERE nombre = 'Azucar';"
        consulta3 = "SELECT cantidad_ml_g FROM Productos WHERE nombre = 'Agua';"

        limon = self.mysql.execute(consulta1)
        azucar = self.mysql.execute(consulta2)
        agua = self.mysql.execute(consulta3)

        for l in limon:
            cant_limon = l[0]

        for a in azucar:
            cant_azucar = a[0]

        for a in agua:
            cant_agua = a[0]

        if cant_limon >= 500 and cant_azucar >= 100 and cant_agua >= 500:
            return True
        else:
            return False

    def vender_limonada(self):
        if self.comprobar_limonada():
            consulta = "UPDATE Productos SET cantidad_ml_g = cantidad_ml_g - 250 WHERE nombre = 'Limonada';"

            self.mysql.execute(consulta)
            self.mysql.commit()
            print("Se ha vendido 1 vaso de limonada")
        else:
            print("No hay mas limonada para vender")

    def comprobar_limonada(self):
        consulta = "SELECT cantidad_ml_g FROM Productos WHERE nombre = 'Limonada';"

        limonada = self.mysql.execute(consulta)

        for l in limonada:
            cant_limonada = l[0]

        if cant_limonada >= 250:
            return True
        else:
            return False

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
