import sqlite3

class Libro:

    # Array para mostrar la informacion por pantalla
    id_libro = []
    nombre = []
    autor = []
    genero = []
    editorial = []
    ano = []
    num_copias = []

    def extractInfo(self):
        # Se usa del para no tener datos duplicados
        del self.id_libro[:], self.nombre[:], self.autor[:], self.genero[:], self.editorial[:], self.ano[:], self.num_copias[:]
        sql = sqlite3.connect("Biblioteca_bd.db", timeout=10)

        query = "SELECT * FROM Libro;"
        result = sql.execute(query)

        for libro in result:
            self.id_libro.append(libro[0])
            self.nombre.append(libro[1])
            self.autor.append(libro[2])
            self.genero.append(libro[3])
            self.editorial.append(libro[4])
            self.ano.append(libro[5])
            self.num_copias.append(libro[6])

        self.num = len(self.nombre)
        sql.close()

    def addLibro(self, nombre, autor, genero, editorial, ano):
        sql = sqlite3.connect("Biblioteca_bd.db", timeout=10)
        query = "INSERT INTO Libro(Nombre, Autor, Genero, Editorial, Ano, Num_copias) " \
                "VALUES ('{}', '{}', '{}', '{}', '{}', 1);".format(nombre, autor, genero, editorial, ano)
        sql.execute(query)
        sql.commit()

        print("Se ha insertado un nuevo libro")
        sql.close()