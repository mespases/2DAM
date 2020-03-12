from flask import Flask, render_template, redirect, request
from lector import Lector
from multas import Multa
from prestamo import Prestamo
from libro import Libro

# Clases a usar
app = Flask(__name__)
lector = Lector()
multas = Multa()
prestamo = Prestamo()
libro = Libro()

@app.route('/')
def index():
    return redirect("/libros", code=302)

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

@app.route('/add_libro')
def addLibro():
    return render_template('addLibro.html')

@app.route('/inf_add_libro', methods=['POST'])
def inf_add_libro():
    json = request.form.to_dict()
    libro.addLibro(json.get('Nombre'), json.get('Autor'), json.get('Genero'), json.get('Editorial'), json.get('Ano'))
    return redirect("/libros", code=302)

@app.route('/add_copia_libro')
def addCopiaLibro():
    libro.extractInfo()
    return render_template("copia_libro.html", nombre=libro.nombre, num=libro.num)

@app.route('/inf_add_copia_libro', methods=['POST'])
def inf_add_copia_libro():
    json = request.form.to_dict()
    libro.addCopiaLibro(json.get("Nombre"), json.get("Cantidad"))
    return redirect("/libros", code=302)

@app.route('/pedir_libro')
def pedirLibro():
    libro.extractInfo()
    return render_template("pedir_libro.html", nombre=libro.nombre, num=libro.num, id=libro.id_libro)

@app.route('/inf_pedir_libro', methods=['POST'])
def inf_pedir_libro():
    json = request.form.to_dict()
    prestamo.addPrestamo(json.get("id_libro"), json.get("id_lector"))
    return redirect("/libros", code=302)

if __name__ == "__main__":
    app.debug = True
    app.run()