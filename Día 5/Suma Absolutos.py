def suma_absolutos(*numeros):
    suma=0
    for e in numeros:
       suma+=abs(e)

    return suma

print(suma_absolutos(1,2,3,-4,5,-5))