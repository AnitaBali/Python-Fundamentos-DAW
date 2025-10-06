def numeros_persona(nombre,*args):
    return print(f"{nombre}, la suma de tus números es {sum(args)}")

numeros_persona("Ana",1,2,3,4,5)