from os import remove
from random import *

def lanzar_moneda():
    moneda=['cara','cruz']
    tirada=choice(moneda)

    return tirada

def probar_suerte(resultado,lista):
    if resultado=='cara':
        print("La lista se autodestruirá")
        return []
    elif resultado=='cruz':
        print("La lista fue salvada")
        return lista


lista_numeros=[1,2,3,4,5]
lanzamiento=lanzar_moneda()
print(lanzamiento)
resultado=probar_suerte(lanzamiento,lista_numeros)
print(resultado)