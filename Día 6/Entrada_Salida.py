#Imprimir texto con las líneas en una lista
mi_archivo=open('prueba.txt')
todas=mi_archivo.readlines()

todas=todas.pop()

print(todas)





for l in mi_archivo:
    print("Aquí dice: " + l)

