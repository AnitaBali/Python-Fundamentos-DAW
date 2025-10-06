import re

def verificar_saludo(frase):
    patron=r'^Hola'
    buscar=re.search(patron,frase)
    if buscar:
        print("Ok")
    else:
        print("No has saludado")

verificar_saludo("Hola Ana que tal")