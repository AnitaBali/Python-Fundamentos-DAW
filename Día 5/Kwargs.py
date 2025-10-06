def suma(**kwargs):
    total=0

    for clave, valor in kwargs.items():
        total=total+valor

    return total

misValores=suma(x=1,y=2,z=3)
print(misValores)