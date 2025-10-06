import re

texto= "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

#palabra='ayuda' in texto
#print(palabra)

#Busca solo una vez la palabra ayuda
patron='ayuda'
busqueda=re.search(patron,texto)
#print(busqueda.span()) #Me dara la ubicacion de la palabra a buscar en patron
#print(busqueda.start()) #Me dara la ubicacion de inicio
#print(busqueda.end()) #Me dara la ubicacion de fin

#Busca solo una vez la palabra ayuda
busqueda_completa=re.findall(patron,texto) #Devolvera una lista con las veces que aparezca
print(busqueda_completa)
print(len(busqueda_completa)) #Pongo len si quiere ver el total, si no lo pongo me devolvera la lista
for hallazgo in re.finditer(patron,texto):
    print(hallazgo.span())  #Me devolvera las posiciones de cada vez que aparezca la palabra ayuda