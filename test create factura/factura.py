from datetime import datetime

class pru:

    def __init__(self):
        self.factura("Pedro", "Tv", 15, 24)

    def factura(self, nombre, producto, cantidad, precio):
        total = cantidad * precio

        factura = "\n############################ \n" \
                  "Aparatos S.L. \n" \
                  "Fecha: {}\n" \
                  "Factura a: \n" \
                  "Nombre: {} \n" \
                  "Producto comprado: {} \n" \
                  "Cantidad: {} \n" \
                  "Precio individual: {} \n" \
                  "Precio total: {} \n" \
                  "############################".format(datetime.now().date(), nombre, producto, cantidad, precio, total)

        self.guardarFactura(factura)


    def guardarFactura(self, factura):
        file = open("C:\Users\miguel.espases\Documents\Miguel Espases\Pruebas y demas\stock.txt", "a")

        file.write(factura)

        file.close()

pru()
