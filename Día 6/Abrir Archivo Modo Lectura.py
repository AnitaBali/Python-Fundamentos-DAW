#Modo solo lectura, no se puede escribir, dara error: io.UnsupportedOperation: not writable
#'r' significa solo lectura, read
mi_archivo=open('prueba.txt','r')
mi_archivo.write('Soy el nuevo texto')

mi_archivo.close()