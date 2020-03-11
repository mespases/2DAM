from flask import Flask, render_template
from lector import Lector
from multas import Multa
from prestamo import Prestamo
from libro import Libro
import sqlite3

# Clases a usar
app = Flask(__name__)
lector = Lector()
multas = Multa()
prestamo = Prestamo()
libro = Libro()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/lectores')
def mostrarLector():
    lector.extractInfo()
    return render_template("Lectores.html", nombre=lector.nombre, telefono=lector.telefono,
                           direccion=lector.direccion, num_libros=lector.num_libros_prestados,
                           dias_multa=lector.dias_multa, num=lector.num)

@app.route('/libros')
def mostrarLibro():
    libro.extractInfo()
    return render_template("Libros.html", nombre=libro.nombre, autor=libro.autor, genero=libro.genero,
                           editorial=libro.editorial, ano=libro.ano, num_copias=libro.num_copias, num=libro.num)

@app.route('/prestamos')
def mostrarPrestamo():
    prestamo.extractInfo()
    return render_template("Prestamos.html", lector=prestamo.nombre_lector, libro=prestamo.nombre_libro,
                           fecha_inicio=prestamo.fecha_inicio, fecha_fin=prestamo.fecha_final, num=prestamo.num)

@app.route('/multas')
def mostrarMultas():
    multas.extractInfo()
    return render_template("Multas.html", lector=multas.nombre_lector, num_multas=multas.num_multas, num=multas.num)

if __name__ == "__main__":
    app.debug = True
    app.run()