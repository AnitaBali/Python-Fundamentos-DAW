from collections import Counter
from traceback import print_tb

numeros=[8,6,3,2,4,9,0,1,2,4,5,6,7,4,2,1,3,5,7,7,3,2]
frase="al pan pan y al vino vino"
print(Counter(numeros))
print(Counter(frase))
print(Counter(frase.split()))

serie=Counter([1,2,3,1,1,2,3,4,1,2,3,2,1])
print(serie.most_common(2)) #Me dara los valores  y las veces que se repiten

print(serie.values()) #Imprime los valores
print(serie.total()) #Imprime el total de la suma de los valores, sin contar repetidos
print(serie.pop(1)) #Borra el último valor de la lista
print(serie.values()) #Imprime los valores
print(serie.items()) #Me dara los valores  y las veces que se repiten





