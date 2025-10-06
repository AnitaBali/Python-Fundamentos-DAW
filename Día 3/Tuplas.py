from traceback import print_tb

mi_tuple = (1,"dos", [3.33,"cuatro"], (5.0, 6))

nueva=(1,2,3,4)
print(type(nueva))

a=(1,1.5,"Ana","Loco",3,5.6,(10,20))
print(a[6][0])
#Imprimirá el índice 5, que es el valor 5.6

b=list(a)
print(type(b))

t=(1,2,3,4,1)
print(t.count(1))
print(t.index(4))