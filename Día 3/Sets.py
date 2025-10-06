#Podemos declarar tuples, pero no listas ni diccionarios
mi_set=set((1,2,3,4,5))
print(type(mi_set))
print(len(mi_set))

#Consultar si hay un elemento en el set
print(2 in mi_set)
#Valor boleeano, dará True

#Unión de sets
s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)
print(s3)

#Mét. add
s1.add(4)
print(s1)

#Mét. remove
#s1.remove(3)
#print(s1)

#Mét. discard
#s1.discard(2)
#print(s1)

#Mét. pop, eliminará un elemento aleatorio
sorteo=s1.pop()
print(sorteo)

#Mét. clear, vaciar el set
s1.clear()
print(s1)