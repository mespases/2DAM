texto = open("C:/Users/miguel.espases/Documents/Miguel Espases/Pruebas y demas/stock.txt", "r+")



lista = []

for i in texto:
    if "[" in i:
        lista.append(i)
    else:
        lista.append(i.split(","))



cant = int(lista[1][1])

if cant <= 15:
    cant += 10

lista[1][1] = str(cant)


texto_fin = open("C:/Users/miguel.espases/Documents/Miguel Espases/Pruebas y demas/stock.txt", "w")
for i in lista:
    if "Nombre" in i:
        texto_fin.write(str(i))
    else:
        print i
        escribir = str(i)
        escribir = escribir.replace("[", "")
        escribir = escribir.replace("]", "")
        escribir = escribir.replace("'", "")
        escribir = escribir.replace("\n", "")
        texto_fin.write(escribir)

texto_fin.close()
print escribir

texto.close()
