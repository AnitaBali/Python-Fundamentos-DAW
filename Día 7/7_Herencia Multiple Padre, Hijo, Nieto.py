class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja,ja")

    def hablar(self):
        print("Adios")


class Hijo(Padre,Madre):   #Aquí al poner Padre primero, heredara primero de padre
    pass

class Nieto(Hijo):
    pass

mi_nieto=Nieto()

mi_nieto.hablar()  #Imprime Hola, no Adios, ya que primero heredo de padre
mi_nieto.reir()
print(Nieto.__mro__)  #Vemos el orden de herencia por clase