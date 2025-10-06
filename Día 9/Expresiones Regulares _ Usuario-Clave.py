import re
clave=input("Clave: ")

patron=r'\D{1}\w{7}'  #Clave que empiece por una letra y luego 7 caracteres alfanumericos, debe cumplirse

chequear=re.search(patron,clave)
print(chequear)