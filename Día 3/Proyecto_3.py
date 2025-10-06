#Primero doy bienvenida al usuario y luego le pido que introduzca un texto
from itertools import count
print("---------------------BIENVENIDO---------------------")
texto=input("Usuario, introduzca un texto: ")

#Segundo, el texto pasado por el usuario lo convierto en lista con los caracteres en minúscula
lista=list(texto.lower())
#print(lista)

#Tercero, le pido al usuario que introduzca tres letras y que las almacene en una lista
letra1=input("Ingrese una primera letra a su elección: ").lower()
letra2=input("Ingrese una segunda letra a su elección: ").lower()
letra3=input("Ingrese una última letra a su elección: ").lower()
letras=[letra1,letra2,letra3]
#print(type(letras))

#Cuarto, contar cuantas veces aparece la letra indicada
print("\n")
print("LETRAS REPETIDAS")
contar1=lista.count(letra1)
print(f"La letra '{letra1}' aparece un total de {contar1} veces.")

contar2=lista.count(letra2)
print(f"La letra '{letra2}' aparece un total de {contar2} veces.")

contar3=lista.count(letra3)
print(f"La letra '{letra3}' aparece un total de {contar3} veces.")

#Quinto, decir cuantas palabras hay en el texto
print("\n")
print("PALABRAS TOTALES")
palabras=texto.split()
numeroPalabras=len(palabras)
print(f"Hay un total de {numeroPalabras} palabras.")

#Sexto, decir la primera y última letra del texto
print("\n")
print("PRIMERA Y ÚLTIMA LETRA")
primera=lista[0]
print(f"La primera letra es: {primera}")
ultima=lista[-1]
print(f"La última letra es: {ultima}")

#Séptimo, invertir orden de la lista y leer en texto
print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
textoInvertido=' '.join(palabras) #Unir palabras poniendo un espacio
print(textoInvertido)

#Comprobar si esta la palabra "Python"
print("\n")
print("BUSCAR PALABRA 'PYTHON'")
comprobar="python" in texto
dic={True:"si",False:"no"}
print(f"La palabra 'python' {dic[comprobar]} se encuentra en el texto.")

