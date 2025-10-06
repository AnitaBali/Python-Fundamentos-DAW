def generacion():
    x=1
    yield x

    x += 1
    yield x

    x += 1
    yield x


g=generacion()
print(next(g))
print(next(g))
print(next(g))
