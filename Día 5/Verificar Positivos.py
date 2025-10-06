lista_numeros = [1, 2, 3, -5]

def todos_positivos(lista):
    for n in lista:
        if n < 0:
            return False
        else:
            pass
    return True

print(todos_positivos(lista_numeros))