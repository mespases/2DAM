from Banco import Banco
from BD import BD

class CRM:

    banco = Banco()
    bd = BD()

    def menu(self):
        """ Bucle del menu hasta que se inserte la opcion de
            salir del menu, este imprime el menu y permite
            seleccionar la opcion """
        opcion = 0
        while opcion != 7:
            self.__printOpciones()
            opcion = int(input("\nIntroduce una opcion: "))
            self.__elegirOpcionesMenu(opcion)

    def __printOpciones(self):
        """ Imprime por pantalla las opciones disponibles para elegir
            en el menu """
        print("\n================Menu================")
        print("1) Vender")
        print("2) Precio por producto")
        print("3) Ver media de articulos por venta")
        print("4) Media ingresos de tienda")
        print("5) Top 5 productos mas vendidos")
        print("6) Top 5 productos menos vendidos")
        print("7) Salir del menu")

    def __printOpcionesSecundarias(self, mediasDe):
        """ Imprime las opciones secundarias disponibles en el
            submenu """
        if mediasDe == "articulos":
            print("\n===========Medias de articulo===========")
            print("1) Media dia")
            print("2) Media mes")
            print("3) Media trimestre")
            print("4) Media anyo")
        elif mediasDe == "tienda":
            print("\n===========Medias de tienda===========")
            print("1) Media dia")
            print("2) Media mes")
            print("3) Media trimestre")
            print("4) Media anyo")

    def __elegirOpcionesMenu(self, opcion):
        """ Selecciona la opcion elegida en el menu y posteriormente
            hara el metodo correspondiente para cada opcion elegida """
        if opcion == 1:
            self.__vender()
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            self.__printOpcionesSecundarias("articulos")
            opcionSecundaria = int(input("\nIntroduce una opcion: "))
        elif opcion == 6:
            self.__printOpcionesSecundarias("tienda")
            opcionSecundaria = int(input("\nIntroduce una opcion: "))
        elif opcion == 7:
            print("Saliendo del menu")
            self.bd.sql.close()
        else:
            print("La opcion insertada es incorrecta")

    def __elegirOpcionesMenuSecundarias(self, mediasDe, opcionesSecundarias):
        """ Selecciona la opcion elegida del submenu y posteriormente
            hara el metodo correspondiente para cada opcion elegida """
        if mediasDe == "articulos":
            if opcionesSecundarias == 1:
                pass
            elif opcionesSecundarias == 2:
                pass
            elif opcionesSecundarias == 3:
                pass
            elif opcionesSecundarias == 4:
                pass

        elif mediasDe == "tienda":
            if opcionesSecundarias == 1:
                pass
            elif opcionesSecundarias == 2:
                pass
            elif opcionesSecundarias == 3:
                pass
            elif opcionesSecundarias == 4:
                pass

    def __vender(self):
        """ Vende el producto seleccionado y pide al cliente si
            quiere factura o no """
        self.bd.selectProductos()
        producto = raw_input("\nQue producto vas a comprar: ")
        if producto.title() in self.bd.productos:
            cantidad = int(raw_input("Introduce la cantidad deseada: "))
            nombre = raw_input("\nNombre del cliente: ")

            factura = raw_input("Quiere factura, S/N: ")
            if factura.upper() == "S":
                self.__crearFactura(cantidad, nombre, producto.title())
                self.bd.sumarCantidades(producto, cantidad)
                self.banco.realizarPago()
        else:
            print("El producto insertado no es correcto")

    def __crearFactura(self, cantidad, nombre, producto):
        """ Crea la factura del cliente """
        total = self.bd.crearFacturaBD(producto, cantidad, nombre)
        print("\nFACTURA")
        print("El nombre del cliente es: {}").format(nombre)
        print("El producto comprado del cliente es: {}").format(producto)
        print("La cantidad del producto del cliente es: {}").format(cantidad)
        print("El total de la factura es: {}\n").format(total)

a = CRM()
a.menu()