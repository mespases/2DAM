# coding=utf-8
import sqlite3

class BD:

    # Conexion mysql
    sql = sqlite3.connect("C:\Users\miguel.espases\Desktop\ea.db", timeout=10)
    cursor = sql.cursor()

    def insertJugadores(self):
        """ Inserta nuevos jugadores en la bd """
        try:
            nombre = "z"
            nick = "z"
            edad = 1
            equipo = "E1"
            consulta = "INSERT INTO 'Jugadores' VALUES ('{}', '{}', {}, '{}');".format(nombre, nick, edad, equipo)

            self.sql.execute(consulta)
            self.sql.commit()
        except:
            print("Fallo al intentar meter un jugador")

    def insertEquipos(self):
        """ Inserta nuevos equipos en la bd """
        try:
            nombre = "Master"
            camp_cagado = 5
            consulta = "INSERT INTO 'Equipos' VALUES ('{}', {});".format(nombre, camp_cagado)

            self.sql.execute(consulta)
            self.sql.commit()
        except:
            print("Fallo al intentar meter un equipo")

    def insertCampeonatos(self):
        """ Inserta nuevos campeonatos en la bd """
        try:
            nombre = "gg"
            consulta = "INSERT INTO 'Campeonato'('Nombre') VALUES ('{}');".format(nombre)

            self.sql.execute(consulta)
            self.sql.commit()
        except:
            print("Error al intentar insertar un campeonato")

    def cantidadEquipos(self):
        """ Devuelve la cantidad de equipos en la bd """
        consulta = "SELECT * FROM Equipos"
        result = self.sql.execute(consulta)

        contador = 0
        for i in result:
            contador += 1

        return contador

    def resultadoGenerarPartidos(self, numeros, campeonato):
        """ Guarda en la bd el resultado aleatorio generado """
        lista_equipos = []
        lista_resultados = []
        consulta = "SELECT * FROM Equipos"
        result = self.sql.execute(consulta)

        # Anade a los equipos en la array
        for i in result:
            lista_equipos.append(i[0])

        # Anade a lista de resultados: ej: numeros = [7,3,1,6,5,4,2,8]
        # i = 0, numeros[i] -> posicion i 0 = 7 / siguiente iteracion.  i = 1, numeros[i] -> posicion i 1 = 3
        # Resultado -> lista_equipos[numeros[i]] == lista_equipos[7] / siguiente iteracion. lista_equipos[numeros[i]] == lista_equipos[3]
        for i in range(8):
            lista_resultados.append(lista_equipos[numeros[i]])

        insert1 = "INSERT INTO Partidos(Campeonato, Equipo1, Equipo2, Ronda) VALUES ('{}', '{}', '{}', 'Cuartos');".format(campeonato, lista_resultados[0], lista_resultados[1])
        insert2 = "INSERT INTO Partidos(Campeonato, Equipo1, Equipo2, Ronda) VALUES ('{}', '{}', '{}', 'Cuartos');".format(campeonato, lista_resultados[2], lista_resultados[3])
        insert3 = "INSERT INTO Partidos(Campeonato, Equipo1, Equipo2, Ronda) VALUES ('{}', '{}', '{}', 'Cuartos');".format(campeonato, lista_resultados[4], lista_resultados[5])
        insert4 = "INSERT INTO Partidos(Campeonato, Equipo1, Equipo2, Ronda) VALUES ('{}', '{}', '{}', 'Cuartos');".format(campeonato, lista_resultados[6], lista_resultados[7])

        self.sql.execute(insert1)
        self.sql.execute(insert2)
        self.sql.execute(insert3)
        self.sql.execute(insert4)

        self.sql.commit()

    def ganadoresPartidos(self, lista_ganadores, ronda, campeonato):
        """ Introduce el la bd el ganador del partido """
        consulta = "SELECT * FROM Partidos WHERE Ronda = '{}' AND Ganador IS NULL;".format(ronda)
        result = self.sql.execute(consulta)
        lista_partidos = []

        for i in result:
            lista_partidos.append(i)

        # Introduce el ganador del partido en la bd
        contador = 0
        for i in lista_partidos:
            if lista_ganadores[contador] == 0:
                self.sql.execute("UPDATE Partidos SET Ganador = '{}' WHERE Equipo1 = '{}';".format(i[1], i[1]))
            else:
                self.sql.execute("UPDATE Partidos SET Ganador = '{}' WHERE Equipo1 = '{}';".format(i[2], i[1]))
            contador += 1

        self.sql.commit()
        self.clasificar(ronda, campeonato)

    def clasificar(self, ronda, campeonato):
        """ Clasifica a los ganadores en una ronda mas arriba, ej: Ganador de Cuartos pasa a Semifinal """
        consulta = "SELECT * FROM Partidos WHERE Ronda = '{}' AND Campeonato = {};".format(ronda, campeonato)
        result = self.sql.execute(consulta)
        lista_partidos = []

        for i in result:
            lista_partidos.append(i)

        if ronda == "Cuartos":
            self.sql.execute("INSERT INTO Partidos(Campeonato, Equipo1, Equipo2, Ronda) VALUES ('{}', '{}', '{}', 'Semifinal');".format(campeonato, lista_partidos[0][3], lista_partidos[1][3]))
            self.sql.execute("INSERT INTO Partidos(Campeonato, Equipo1, Equipo2, Ronda) VALUES ('{}', '{}', '{}', 'Semifinal');".format(campeonato, lista_partidos[2][3], lista_partidos[3][3]))
        elif ronda == "Semifinal":
            self.sql.execute("INSERT INTO Partidos(Campeonato, Equipo1, Equipo2, Ronda) VALUES ('{}', '{}', '{}', 'Final');".format(campeonato, lista_partidos[0][3], lista_partidos[1][3]))
        elif ronda == "Final":
            self.sumarPremioEquipoGanador(campeonato)

        self.sql.commit()

    def sumarPremioEquipoGanador(self, campeonato):
        """ Suma al ganador del campeonato 1 campeonato ganado """
        consulta = "SELECT Ganador FROM Partidos WHERE Ronda = 'Final' AND Campeonato = {};".format(campeonato)
        result = self.sql.execute(consulta)

        ganador = []
        for i in result:
            ganador.append(i)

        print("¡¡¡ El equipo {} es el ganador del campeonato !!!".format(ganador[0][0]))
        self.sql.execute("UPDATE Equipos SET Campeonatos_Ganados = Campeonatos_Ganados + 1 WHERE Nombre = '{}';".format(ganador[0][0]))
        self.sql.commit()


    def close_sql(self):
        """ Cierra sqlite """
        self.sql.close()


# a = BD()
#
# a.cantidadEquipos()
# a.close_sql()
