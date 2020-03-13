import sqlite3

class Lector:

    # Array para mostrar la informacion por pantalla
    id_lector = []
    nombre = []
    telefono = []
    direccion = []
    num_libros_prestados = []
    dias_multa = []

    def extractInfo(self):
        """ Extrae toda la informacion de la BD y la anade en arrays """
        # Se usa del para no tener datos duplicados
        del self.id_lector[:], self.nombre[:], self.telefono[:], self.direccion[:], self.num_libros_prestados[:], self.dias_multa[:]
        sql = sqlite3.connect("Biblioteca_bd.db", timeout=10)

        query = "SELECT * from Lector;"
        result = sql.execute(query)

        for lector in result:
            self.id_lector.append(lector[0])
            self.nombre.append(lector[1])
            self.telefono.append(lector[2])
            self.direccion.append(lector[3])
            self.num_libros_prestados.append(lector[4])
            self.dias_multa.append(lector[5])

        self.num = len(self.nombre)
        sql.close()

    def addLector(self, nombre, telefono, direccion):
        """ Anade un lector pasandole todos los parametros especificados """
        sql = sqlite3.connect("Biblioteca_bd.db", timeout=10)
        query = "INSERT INTO Lector (Nombre, Telefono, Direccion, Num_libros_prestados, Dias_multa) " \
                "VALUES ('{}', '{}', '{}', 0, 0);".format(nombre, telefono, direccion)
        sql.execute(query)
        sql.commit()

        print("Se ha insertado un nuevo cliente")
        sql.close()