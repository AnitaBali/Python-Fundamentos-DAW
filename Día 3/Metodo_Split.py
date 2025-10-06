#Creara una lista de cada palabra del texto
texto="Coco es el gato mas hermoso"

resultado=texto.split()
print(resultado)
#Imprimira ['Coco', 'es', 'el', 'gato', 'mas', 'hermoso']

#Separar tomando como referencia un caracter
texto="Coco Coco Coco que lindo"
resultado=texto.split("o")
print(resultado)
#Imprimira ['C', 'c', ' C', 'c', ' C', 'c', '']