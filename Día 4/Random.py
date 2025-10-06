from random import *

#Mét. randint
aleatorio=randint(1,5)
print(aleatorio)
#Cada vez que ejecutemos saldra un número aleatorio entre 1 y 50.

#Mét. uniform
aleatorio=round(uniform(1,5),2)
print(aleatorio)
#Cada vez que ejecutemos saldran números decimales aleatorios entre 1 y 5, con dos decimales

#Mét. random
aleatorio=round(random()*100)
print(aleatorio)
#Imprime un float entre 1 y 10, pero si redondeamos y multiplicamos por 100 dara int entre 1 y 100

#Mét. choice
colores=["blanco","azul","rojo"]
aleatorio=choice(colores)
print(aleatorio)
#Cada vez que se ejecute imprimira un color aleatorio de mi lista

#Mét. shuffle, mezclar
numeros=list(range(5,50,5))
shuffle(numeros)
print(numeros)
