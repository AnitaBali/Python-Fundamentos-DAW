def prueba(num1,num2,*args,**kwargs):
    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")

    for e in args:
        print(f"arg= {e}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

prueba(10,20,3,2,3,4,5,6,1,x="5",y="7")
