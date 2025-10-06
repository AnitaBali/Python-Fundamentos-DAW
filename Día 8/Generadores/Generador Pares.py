def generador(inicio,fin):

    for n in range(inicio,fin+1):
        if n%2==0:
            yield n

g=generador(5,200)
print(next(g))
print(next(g))
print(next(g))
print(next(g))