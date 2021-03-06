# coding=utf-8
from bd import BD

class Tienda:

    datos = BD()

    def __init__(self):
        self.menu()

    def alta_trabajador(self):
        nombre = raw_input("\nIntroduce el nombre del trabajador: ").title()
        edad = int(input("Introduce la edad del trabajador: "))
        self.datos.insert_personal(nombre=nombre, edad=edad)

    def pedido_ingredientes(self):
        producto = raw_input("\nIntroduce el nombre del producto a insertar: ").title()
        cantidad = int(input("Introduce la cantidad que quieres pedir: "))
        self.datos.update_productos(cantidad=cantidad, nombre_producto=producto)

    def producir_limonada(self):
        """ 500 ml de zumo de limón, 500 ml de agua fría, 100 g de azúcar """
        self.datos.producir_productos_1L()

    def vender_limonada(self):
        self.datos.vender_limonada()
        self.datos.update_ganancias_mas_1('Tienda 1')

    def menu(self):
        opcion = 0
        while opcion != 6:
            print("\n--------Menu--------")
            print("1) Dar de alta nuevo trabajador")
            print("2) Pedido de ingredientes en 'gramos'/'ml'")
            print("3) Producir 1L de limonada")
            print("4) Vender limonada")
            print("5) Ver las ganancias de la limonada")
            print("6) Salir")
            opcion = int(input("Introduce una opcion: "))
            self.sub_menu(opcion)

    def sub_menu(self, opcion):
        if opcion == 1:
            self.alta_trabajador()
        elif opcion == 2:
            self.pedido_ingredientes()
        elif opcion == 3:
            self.producir_limonada()
        elif opcion == 4:
            self.vender_limonada()
        elif opcion == 5:
            self.datos.select_ganancias()
        elif opcion == 6:
            self.datos.close_mysql()
            exit(0)
        else:
            print("La opcion introducida es incorrecta")

if __name__ == "__main__":
    Tienda()
