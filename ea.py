from bd import BD
import random

class EA:

    bd = BD()
    campeonato = 2

    def __init__(self):
        pass

    def generarPartidos(self):
        """ Genera partidos aleatorios entre los equipos de la bd """
        numeros = []
        cant_equipos = self.bd.cantidadEquipos()
        self.campeonato = int(input("Introduce el id del campeonato: "))

        while len(numeros) < 8:
            n = random.randrange(cant_equipos[0])
            if n not in numeros:
                numeros.append(n)

        self.bd.resultadoGenerarPartidos(numeros, self.campeonato)

    def jugarPartidos(self):
        """ Genera un ganador de los partidos aleatorio, 0 gana el equipo de la izquierda
            1 gana el de la derecha """
        lista_ganadores = []

        for i in range(4):
            lista_ganadores.append(random.randrange(2))

        self.bd.ganadoresPartidos(lista_ganadores, "Final", self.campeonato)



a = EA()
# a.generarPartidos()
a.jugarPartidos()
a.bd.close_sql()
