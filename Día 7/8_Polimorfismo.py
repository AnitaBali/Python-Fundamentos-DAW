class Vaca:

    def __init__(self,nombre):
        self.nombre=nombre

    def hablar(self):
        print(self.nombre + " dice muuuu")

class Oveja:

    def __init__(self,nombre):
        self.nombre=nombre

    def hablar(self):
        print(self.nombre + " dice beee")


milka=Vaca("Milka")
dolly=Oveja("Dolly")

animales=[milka,dolly]

for e in animales:
    e.hablar() #Llamo a cada elemento de la lista y el metodo que quiero


def animal_habla(animal):
    animal.hablar()

animal_habla(milka)
animal_habla(dolly)