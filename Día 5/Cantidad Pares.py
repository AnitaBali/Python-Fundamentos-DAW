lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

def cantidad_pares(lista):
    pares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
    return pares


print(cantidad_pares(lista_numeros))