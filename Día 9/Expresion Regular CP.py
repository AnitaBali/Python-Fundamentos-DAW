import re

def verificar_cp(cp):

    patron=r'\w{2}\d{4}'
    comprobar=re.search(patron,cp)
    if comprobar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

verificar_cp("a1234a")