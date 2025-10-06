def suma_cuadrados(*numeros):
    suma=0

    for elementos in numeros:
        cuadrado=elementos**2
        suma=suma+cuadrado

    return suma


print(suma_cuadrados(1,2,3))