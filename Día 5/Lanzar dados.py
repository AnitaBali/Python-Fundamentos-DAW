from random import *

def lanzar():
    dado=randint(1,6)

    return dado

def evaluar_jugada(dado1,dado2):
    suma_dados=dado1+dado2
    if suma_dados<=6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif 6<suma_dados<10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

    return suma_dados

tirada1=lanzar()
tirada2=lanzar()
resultado=evaluar_jugada(tirada1,tirada2)
print(resultado)

