import re

#Buscar un patrón,debe cumplir el patrón

texto="llama al 564-525-6588 ya mismo"

patron=re.compile(r'(\d{3})-(\d{3})-(\d{4})') #Compila en tres grupos: 1 - 2 -3

resultado=re.search(patron,texto)
print(resultado) #Veremos si el patrónse cumple en el texto
print(resultado.group()) #Nos dará el resultado si se localiza exacto el patrón en el texto
print(resultado.group(3)) #Devolvera la parte 3 del listado creado