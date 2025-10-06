from random import *
# Lista inicial
palitos=['--','---','----','-----']

# Mezclar los palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#Pedirle al usuario intento
def intento():
    intento=''

    while intento not in ['1','2','3','4']:
        intento=input("Elige un numero del 1 al 4: ")

    return int(intento)

#Comprobar intento
def comprobar(lista,intento):
        if lista[intento-1]=='-':
            print('A lavar los platos.')
        else:
            print('Te has salvado.')

        print(f"Te ha tocado {lista[intento-1]}.")

palitos_mezclados=mezclar(palitos)
seleccion=intento()
chequear=comprobar(palitos_mezclados,seleccion)