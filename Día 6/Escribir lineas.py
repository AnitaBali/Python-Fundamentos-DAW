#Escribir strings como una lista, usando un bucle para que haga el salto de línea por elemento de la lista
mi_archivo=open('prueba1.txt','w')

lista=['hola','mundo','aqui','estoy']
for p in lista:
    mi_archivo.writelines(p+'\n')


mi_archivo.close()