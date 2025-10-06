import re

texto="No atendemos los lunes por la tarde"

buscar=re.search(r'lunes|martes',texto)  #Buscara que este lunes o martes en el texto

#Palabra comodin
buscar2=re.search(r'....demos....',texto)  #Los puntos hacen de comodin, cuantos mas pongamos mas letras

#Que el texto no empiece por un digito, el sombrerito se pone primero para indicar que empiece
buscar3=re.search(r'^\D',texto)

#Que el texto no termine en un digito, el signo dolar se pone al final para indicar que termine
buscar4=re.search(r'\D$',texto)

#Incluir los caracteres que no sean espacios vacíos o en blanco, si añado el + me dará las palabras, si no las letras
buscar5=re.findall(r'[^\s]+',texto)

print(buscar)
print(buscar2)
print(buscar3)
print(buscar4)
print(buscar5)
print(''.join(buscar5)) #Para imprimir sin espacios en blanco