class Pajaro:

    alas=True

    def __init__(self,color,especie):
        self.color=color
        self.especie=especie

mi_pajaro=Pajaro("rosa","canario")

print(f"Mi pájaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}.")
print(mi_pajaro.alas)