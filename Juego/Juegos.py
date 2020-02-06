import random

class Juegos:

    __ofertas = ["Juegos al 15%", "Libros 2x1", "Peliculas 3x2", "Black Friday "]

    def __anadir_cliente(self):
        nombre = raw_input("Introduce el nombre del cliente: ")
        dni = raw_input("Introduce el dni del cliente: ")
        fecha_nacimiento = raw_input("Introduce la fecha del cliente: ")
        direccion = raw_input("Introduce la direccion del clinete: ")
        localidad = raw_input("Introduce la localidad del cliente: ")
        municipio = raw_input("Introduce el municipio del cliente: ")
        codigo_postal = raw_input("Introduce el codigo postal del cliente: ")
        correo = raw_input("Introduce el correo del cliente")
        ley = raw_input("Aceptas la ley de proteccion de datos ? S/N ")
        if ley.upper() == "S":
            ley_aceptada = True
        else:
            ley_aceptada = False

        intereses = raw_input("Introduce un interes del cliente: ")

    def __anadir_nuevos_intereses(self):
        dni = raw_input("Introduce el dni del cliente al cual le quiere anadir un nuevo interes\n>")

    def __imprimir_ofertas(self):
        num = random.randrange(4)
        print("La oferta de hoy es {}".format(self.__ofertas[num]))

    def __cambiar_cliente_a_potencial(self):
        pass

    def menu(self):
        opcion = 0

        while opcion != 4:
            self.printMenu()
            opcion = int(input("> "))

            if opcion == 1:
                self.__anadir_cliente()

            elif opcion == 2:
                self.__anadir_nuevos_intereses()

            elif opcion == 3:
                self.__imprimir_ofertas()

            elif opcion == 4:
                print("Saliendo del programa")

            else:
                print("Te has equivocado de opcion")

            self.__cambiar_cliente_a_potencial()

    def printMenu(self):
        print("==========Menu==========")
        print("1) Anadir cliente")
        print("2) Anadir nuevos intereses")
        print("3) Imprimir ofertas")
        print("4) Salir del programa")


a = Juegos()
a.menu()
