from bd import BD
import random

class EA:

    bd = BD()
    # campeonato = 10

    def __init__(self):
        self.menu()

    def menu(self):
        opcion = 0
        while opcion != 3:
            opcion = int(input("Introduce una opcion: "))

            if opcion == 1:
                self.generarPartidos()
            elif opcion == 2:
                self.jugarPartidos()
            elif opcion == 3:
                self.bd.close_sql()


    def generarPartidos(self):
        """ Genera partidos aleatorios entre los equipos de la bd """
        numeros = []
        cant_equipos = self.bd.cantidadEquipos()
        self.campeonato = int(input("Introduce el id del campeonato: "))

        while len(numeros) < 8:
            n = random.randrange(cant_equipos)
            if n not in numeros:
                numeros.append(n)

        self.bd.resultadoGenerarPartidos(numeros, self.campeonato)

    def jugarPartidos(self):
        """ Genera un ganador de los partidos aleatorio, 0 gana el equipo de la izquierda
            1 gana el de la derecha """
        lista_ganadores = []

        for i in range(4):
            lista_ganadores.append(random.randrange(2))

        for i in range(3):
            if i == 0:
                self.bd.ganadoresPartidos(lista_ganadores, "Cuartos", self.campeonato)
            elif i == 1:
                self.bd.ganadoresPartidos(lista_ganadores, "Semifinal", self.campeonato)
            elif i == 2:
                self.bd.ganadoresPartidos(lista_ganadores, "Final", self.campeonato)


a = EA()
