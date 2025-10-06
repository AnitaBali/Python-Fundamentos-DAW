def decorar_saludo(funcion):

    def otra(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    return otra

@decorar_saludo
def mayuscula(texto):
        print(texto.upper())

@decorar_saludo
def minuscula(texto):
        print(texto.lower())

mayuscula("Ana")
