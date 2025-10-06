from itertools import count
from random import *

diccionario=["copiloto","exoplaneta","veneno","dorado","torre","galgo"]
letras_correctas=[]
letras_incorrectas=[]
intentos=6
aciertos=0
juego_terminado=False

def palabra_a_adivinar(lista):
    adivinar=choice(lista)
    letras_unicas=len(set(adivinar))
    return adivinar,letras_unicas

def guiones_palabra(palabra):
    print("Bienvenido usuario, debe adivinar la letra escondida entre guiones: ")
    for letra in palabra:
        print("_",end=" ")
    print("")
    print("")

def validar_letra(letra):
    lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    while letra!=lista:
        if letra in lista:
            print("La letra es válida.")
            break
        elif letra not in lista:
            print("El carácter introducido no es una letra.")
            letra = input("Introduzca una letra: ")








mix=palabra_a_adivinar(diccionario)
guiones_palabra(mix)
letra_usuario=input("Usuario dame una letra: ").lower()
validar_letra(letra_usuario)


