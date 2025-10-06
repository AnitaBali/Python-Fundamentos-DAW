from collections import deque

from collections import deque

cola = deque(['a', 'b', 'c'])
cola.appendleft('d')
print(cola) # Output: deque(['d', 'a', 'b', 'c'])



lista_ciudades=deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
lista_ciudades.appendleft("Mexico")
print(lista_ciudades)
