from Banco import Banco
from BD import BD

class CRM:

    banco = Banco()
    bd = BD()
    dia = 1
    mes = 1
    anyo = 1

    def menu(self):
        """ Bucle del menu hasta que se inserte la opcion de
            salir del menu, este imprime el menu y permite
            seleccionar la opcion """
        opcion = 0
        while opcion != 10:
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
        print("7) Simular paso de dia")
        print("8) Simular paso de mes")
        print("9) Simular paso de anyo")
        print("10) Salir del menu")

    def __printOpcionesSecundarias(self, mediasDe):
        """ Imprime las opciones secundarias disponibles en el
            submenu """
        if mediasDe == "mas":
            print("\n===========Medias de articulo mas vendido===========")
            print("1) Media dia")
            print("2) Media mes")
            print("3) Media trimestre")
            print("4) Media anyo")
        elif mediasDe == "menos":
            print("\n===========Medias de articulo menos vendido===========")
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
            self.bd.selectProductos()
            producto = raw_input("De que producto quieres ver el precio: ")
            self.bd.getPrecio(producto.title())
        elif opcion == 3:
            self.bd.getMediaNumArticulos()
        elif opcion == 4:
            self.bd.getTotalIngresos()
        elif opcion == 5:
            self.__printOpcionesSecundarias("mas")
            opcionSecundaria = int(input("\nIntroduce una opcion: "))
            self.__elegirOpcionesMenuSecundarias("mas", opcionSecundaria)
        elif opcion == 6:
            self.__printOpcionesSecundarias("menos")
            opcionSecundaria = int(input("\nIntroduce una opcion: "))
            self.__elegirOpcionesMenuSecundarias("menos", opcionSecundaria)
        elif opcion == 7:
            self.dia += 1
            self.bd.resetearCantVendida("diaria")
            print("Se ha pasado de dia\n")
        elif opcion == 8:
            self.mes += 1
            self.bd.resetearCantVendida("mensual")
            print("Se ha pasado de mes")
            if self.mes % 3 == 0:
                self.bd.resetearCantVendida("trimestral")
                print("Se han pasado 3 meses")
        elif opcion == 9:
            self.anyo += 1
            self.bd.resetearCantVendida("anual")
            print("Se ha pasado un anyo")
        elif opcion == 10:
            print("Saliendo del menu")
            self.bd.sql.close()
        else:
            print("La opcion insertada es incorrecta")

    def __elegirOpcionesMenuSecundarias(self, mediasDe, opcionesSecundarias):
        """ Selecciona la opcion elegida del submenu y posteriormente
            hara el metodo correspondiente para cada opcion elegida """
        if mediasDe == "mas":
            if opcionesSecundarias == 1:
                self.bd.getProductosMasVendidos("diaria")
            elif opcionesSecundarias == 2:
                self.bd.getProductosMasVendidos("mensual")
            elif opcionesSecundarias == 3:
                self.bd.getProductosMasVendidos("trimestral")
            elif opcionesSecundarias == 4:
                self.bd.getProductosMasVendidos("anual")

        elif mediasDe == "menos":
            if opcionesSecundarias == 1:
                self.bd.getProductosMenosVendidos("diaria")
            elif opcionesSecundarias == 2:
                self.bd.getProductosMenosVendidos("mensual")
            elif opcionesSecundarias == 3:
                self.bd.getProductosMenosVendidos("trimestral")
            elif opcionesSecundarias == 4:
                self.bd.getProductosMenosVendidos("anual")

    def __vender(self):
        """ Vende el producto seleccionado y pide al cliente si
            quiere factura o no """
        self.bd.selectProductos()
        producto = raw_input("\nQue producto vas a comprar: ")
        if producto.title() in self.bd.productos:
            cantidad = int(input("Introduce la cantidad deseada: "))
            nombre = raw_input("\nNombre del cliente: ")

            factura = raw_input("Quiere factura, S/N: ")
            if factura.upper() == "S":
                self.__crearFactura(cantidad, nombre, producto.title())

            self.bd.sumarCantidades(producto.title(), cantidad)
            self.banco.realizarPago()
        else:
            print("El producto insertado no es correcto")

    def __crearFactura(self, cantidad, nombre, producto):
        """ Crea la factura del cliente """
        total = self.bd.crearFacturaBD(producto.title(), cantidad, nombre)
        print("\nFACTURA")
        print("El nombre del cliente es: {}").format(nombre)
        print("El producto comprado del cliente es: {}").format(producto)
        print("La cantidad del producto del cliente es: {}").format(cantidad)
        print("El total de la factura es: {}\n").format(total)

a = CRM()
a.menu()