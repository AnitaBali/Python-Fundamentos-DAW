#Ver el largo de una lista
from idlelib.replace import replace

mi_lista=['a','b','c']
resultado=len(mi_lista)
print(resultado)

#Sobreescribir elemento de la lista
nombres=["Ana","Borja","Fatima","Sergio","Nuria"]
apellidos=["Garcia","Miranda","Reyes","Gomez"]
union=nombres+apellidos
union[0]="Anita"
print(union[0])
#Cambiará Ana por Anita

union.append("Coco")
print(union)
eliminado=union.pop(2)
print(eliminado)

abecedario=["g","h","z","x","e","a"]
abecedario.sort()
print(abecedario)
#Imprimira ['a', 'e', 'g', 'h', 'x', 'z']

abecedario.reverse()
print(abecedario)
#Imprimira ['z', 'x', 'h', 'g', 'e', 'a']