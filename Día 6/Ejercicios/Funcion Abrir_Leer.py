def abrir_leer(archivo):
    archivo=open(archivo)
    return archivo.read()

leer=abrir_leer('Hola.txt')
print(leer)
