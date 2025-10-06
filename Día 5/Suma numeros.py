lista_numeros = [1, 2, 3, 4, 5,999]

def suma_menores(lista):
    suma=0
    for numero in lista:
        if numero>0 and numero<1000:
            suma = suma + numero
    return suma


print(suma_menores(lista_numeros))
