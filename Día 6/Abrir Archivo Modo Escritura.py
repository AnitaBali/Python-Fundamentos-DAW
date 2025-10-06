#Modo escritura, pondremos titulo de nuevo archivo y creara el documento con lo escrito
#'w' significa solo lectura, read
mi_archivo=open('prueba1.txt','w')
mi_archivo.write('Soy el nuevo texto')

mi_archivo.close()