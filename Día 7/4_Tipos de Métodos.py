class Pajaro:

    alas=True

    def __init__(self,color,especie):
        self.color=color
        self.especie=especie

    def piar(self):   #Mét. de instancia
        print('pio pio, mi color es {}'.format(self.color))

    def volar(self,metros):  #Mét. de instancia
        print(f"El pájaro ha volado {metros} metros.")
        self.piar()

    def pintar_negro(self):
        self.color="negro"
        print(f"Ahora el pájaro es {self.color}")

    @classmethod
    def poner_huevos(cls,cantidad):   #Met. de clase
        print(f"Puso {cantidad} huevos.")
        cls.alas=False
        print(Pajaro.alas)

    @staticmethod
    def mirar():    #Mét. estático
        print("El pájaro mira.")




Pajaro.poner_huevos(3)   #No necesita un objeto o instancia para ejecutarse
Pajaro.mirar()
piolin=Pajaro("amarillo","canario")
piolin.pintar_negro()
piolin.volar(50)
piolin.alas=False
piolin.poner_huevos(5)
print(piolin.alas)