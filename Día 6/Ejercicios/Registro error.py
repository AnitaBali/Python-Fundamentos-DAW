def registro_error(archivo):
    archivo=open(archivo,'a')
    archivo.write("se ha registrado un error de ejecución")
    archivo.close()

registro_error("Hola.txt")