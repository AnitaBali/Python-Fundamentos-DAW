def mi_funcion():
    return 4

def mi_generador():
    yield 4

g=mi_generador()
print(mi_funcion())
print(next(g)) #Accede
