def describir_persona(nombre,**kwargs):
    print(f"Características de {nombre}")
    for clave,valor in kwargs.items():
        print(f"{clave}: {valor}")

describir_persona("Ana",color_ojos='marrón',color_pelo='castaño',altura=1.70,peso=55)