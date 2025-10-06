from collections import namedtuple

Persona=namedtuple('Persona',['nombre','altura','peso'])
Ana=Persona('Ana',1.70,55)

print(Ana.altura)
print(Ana.peso)