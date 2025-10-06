#Ver el valor más bajo
menor=min(100,34,91,4,34,56,21)
print(menor)
#Imprime: 4

#Ver el valor más alto
mayor=max(100,34,91,4,34,56,21)
print(mayor)
#Imprime: 100


#Número más alto o bajo de una lista
lista=[100,34,91,4,34,56,21]
print(max(lista))
print(min(lista))


#Listas de string
nombres=['juan','pablo','alicia','carlos']
print(min(nombres))
#Imprime alicia, que es el primero por orden alfabetico
print(max(nombres))
#Imprime pablo que es el último por orden alfabético

#String
texto_ana="guapa"
print(min(texto_ana))
print(max(texto_ana))


#Diccionarios
dic={'C1':45,'C2':11}

print(min(dic.values()))  #11
print(min(dic))           #C1
print(min(dic.items()))   #('C1', 45)
print(min(dic.keys()))    #C1
