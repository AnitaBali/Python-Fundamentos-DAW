def numeros_perfumeria():
    for n in range(1,10000):
        yield f"P - {n}"

def numeros_farmacia():
    for n in range(1,10000):
        yield f"F - {n}"

def numeros_cosmetica():
    for n in range(1,10000):
        yield f"C - {n}"

p=numeros_perfumeria()
c=numeros_cosmetica()
f=numeros_farmacia()

def decorador(rubro):
    print("\n" + "*"*23)
    print("Sú número es: ")
    if rubro=="P":
        print(next(p))
    elif rubro=="F":
        print(next(f))
    else:
        print(next(c))

    print("Aguarde y será atendido.")
    print("*" * 23+"\n")