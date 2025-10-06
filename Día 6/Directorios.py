import os

#ruta=os.getcwd()

#print(ruta)

#Met. para cambiar de directorio, usar doble barra invertida si es WINDOW
#cambiar_ruta=os.chdir('C:\\Users\\LENOVO\\PycharmProjects\\Python\\Prueba')
#archivo=open('otro.txt')
#print(archivo.read())

#Mét. crear directorio
#crear_directorio=os.mkdir('C:\\Users\\LENOVO\\PycharmProjects\\Python\\Prueba\\Nuevo\\prueba.txt')

#Mét. basename
nueva_ruta='C:\\Users\\LENOVO\\PycharmProjects\\Python\\Otro.txt'
elemento=os.path.basename(nueva_ruta)
print(elemento)

#Mét. dirname
nueva_ruta='C:\\Users\\LENOVO\\PycharmProjects\\Python\\Otro.txt'
elemento=os.path.dirname(nueva_ruta)
print(elemento)

#Met. split
nueva_ruta='C:\\Users\\LENOVO\\PycharmProjects\\Python\\Otro.txt'
elemento=os.path.split(nueva_ruta)
print(elemento)

#Eliminar carpetas
os.rmdir('C:\\Users\\LENOVO\\PycharmProjects\\Python\\Prueba\\Nuevo')
#No ejecutara nada, pero si vamos al directorio veremos que borro la carpeta Nuevo
