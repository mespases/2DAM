import sqlite3
import datetime

class Prestamo:

    # Array para mostrar la informacion por pantalla
    id_libro = []
    id_cliente = []
    fecha_inicio = []
    fecha_final = []
    nombre_lector = []
    nombre_libro = []

    def extractInfo(self):
        # Se usa del para no tener datos duplicados
        del self.id_libro[:], self.id_cliente[:], self.fecha_inicio[:], self.fecha_final[:], self.nombre_lector[:], self.nombre_libro[:]
        sql = sqlite3.connect("Biblioteca_bd.db", timeout=10)

        query = "SELECT A.id_libro, A.id_lector, A.Fecha_inicio, A.Fecha_fin, " \
                "B.Nombre, C.Nombre from Prestamo as A INNER JOIN Lector as B on " \
                "A.id_lector = B.id_lector INNER JOIN Libro as C on C.id_libro = A.id_libro;"
        result = sql.execute(query)

        for prestamo in result:
            self.id_libro.append(prestamo[0])
            self.id_cliente.append(prestamo[1])
            self.fecha_inicio.append(prestamo[2])
            self.fecha_final.append(prestamo[3])
            self.nombre_lector.append(prestamo[4])
            self.nombre_libro.append(prestamo[5])

        self.num = len(self.id_libro)
        sql.close()

    def addPrestamo(self, id_libro, id_lector):
        sql = sqlite3.connect("Biblioteca_bd.db", timeout=10)

        fecha_inicio = ""
        fecha_fin = ""

        query = "INSERT INTO Prestamo (id_libro, id_lector, Fecha_inicio, Fecha_fin) " \
                "VALUES ( {}, {}, '{}', '{}');".format(id_libro, id_lector, fecha_inicio, fecha_fin)
        sql.execute(query)
        sql.commit()

        print("Se ha creado un nuevo prestamo")
        sql.close()