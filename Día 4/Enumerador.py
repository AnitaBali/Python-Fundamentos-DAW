#Usando enumerate()
lista=['a','b','c']

for indice,item in enumerate(lista):
    print(indice,item)

#Imprime una serie de tuples:
#0 a
#1 b
#2 c

#Usar enumerate() fuera de un loops, para construir una lista de tuples.
lista=['Ana','Coco','Dolly']

mi_tuple=list(enumerate(lista))
print(mi_tuple)
#Imprime una tuple: [(0, 'Ana'), (1, 'Coco'), (2, 'Dolly')]




