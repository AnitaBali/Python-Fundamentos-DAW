"""
Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros.
- Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor.
- Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
- Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valorintermedio.
"""

def devolver_distintos(a,b,c):
    suma = a + b + c
    mayor=max(a,b,c)
    menor=min(a,b,c)
    intermedio=suma-menor-mayor

    suma=a+b+c

    if suma>15:
        return mayor
    elif suma<10:
        return menor
    else:
        return intermedio


print(devolver_distintos(7,2,4))