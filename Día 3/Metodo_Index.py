
#Ver índice segun posición indicada en otra variable
texto=("Esta es una prueba")
resultado=texto[0]
print(resultado)

#Ver índice segun posición indicada en negativo
texto=("Esta es una prueba")
resultado=texto[-5]
print(resultado)

#Mét. index, primera forma, pasando al index el caracter que buscamos
texto=("Esta es una prueba")
resultado=texto.index("r")
print(resultado)

#Mét. index, segunda forma, pasando al index el caracter que buscamos y desde que posición empezar
texto=("Esta es una prueba")
resultado=texto.index("a",5)
print(resultado)

#Mét. index, segunda forma, pasando al index el caracter que buscamos y desde que posición empezar
#y en que posición terminar
texto=("Esta es una prueba")
resultado=texto.index("a",5,11)
print(resultado)

