import os
import shutil
import send2trash

print(os.getcwd()) #Imprime directorio actual

archivo=open('curso.txt','w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir()) #Lista carpetas del directorio actual

#shutil.move('curso.txt',"C:\\Users\\LENOVO\\OneDrive\\Escritorio") #Mueve archivo a ruta indicada
#shutil.rmtree cuidado porque elimina to con perdida definitiva

send2trash.send2trash('curso.txt') #Lo borra y va a la carpeta de reciclaje, es la forma optima ya que si no se pierde


