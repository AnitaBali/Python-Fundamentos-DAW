def sobrescribir(archivo):
    abrir=open(archivo,'w')
    linea=abrir.write("contenido eliminado")

sobrescribir("Hola.txt")

