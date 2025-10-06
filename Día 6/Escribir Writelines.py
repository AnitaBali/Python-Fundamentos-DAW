archivo=open("registro.txt",'w')
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

for e in registro_ultima_sesion:
   archivo.writelines(e+"\t")

archivo.close()
archivo=open("registro.txt",'r')
leer=archivo.read()
print(leer)