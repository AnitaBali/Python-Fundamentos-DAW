def cantidad_atributos(**kwargs):
    contar=0
    for elemento in kwargs.items():
        contar+=1

    return contar

print(cantidad_atributos(x=1,z=5,a=4,c=2))