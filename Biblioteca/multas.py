import sqlite3

class Multa:

    # Array para mostrar la informacion por pantalla
    id_lector = []
    num_multas = []
    nombre_lector = []

    def extractInfo(self):
        # Se usa del para no tener datos duplicados
        del self.id_lector[:], self.num_multas[:], self.nombre_lector[:]
        sql = sqlite3.connect("Biblioteca_bd.db", timeout=10)

        query = "SELECT A.id_lector, A.Num_multas, B.Nombre FROM Multas as A INNER JOIN Lector as B on A.id_lector = B.id_lector;"
        result = sql.execute(query)

        for multa in result:
            self.id_lector.append(multa[0])
            self.num_multas.append(multa[1])
            self.nombre_lector.append(multa[2])

        self.num = len(self.id_lector)
        sql.close()

    def addFirstMulta(self, id_lector):
        sql = sqlite3.connect("Biblioteca_bd.db", timeout=10)
        query = "INSERT INTO Multas (id_lector, Num_multas) VALUES ({}, 1);".format(id_lector)
        sql.execute(query)
        sql.commit()

        print("Se ha multado por primera vez")
        sql.close()