class Animal:

    def __init__(self,edad,color):
        self.edad=edad
        self.color=color

    def nacer(self):
        print("Este animal ha nacido.")

    def hablar(self):
        print("Este animal emite un sonido")



class Pajaro(Animal):

    def __init__(self,edad, color, altura):
        super().__init__(edad,color)
        self.altura=altura


    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pájaro vuela {metros} metros.")

piolin=Pajaro(2,"azul",60)
coco=Animal(5,"manchado")

piolin.hablar()
piolin.volar(50)
