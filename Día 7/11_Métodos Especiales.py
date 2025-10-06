class CD:

    def __init__(self,autor,titulo,canciones):
        self.autor=autor
        self.titulo=titulo
        self.canciones=canciones

    def __str__(self):  #Modificar la forma de lectura cuando se quiera imprimir el objeto
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):  #No se puede usar si no se implementa en nuestra clase
        return self.canciones

    def __del__(self):  #Elimina
        print("Se ha eliminado el CD.")



mi_cd=CD("Arde Bogota","Cowboys de la A3",15)
print(len(mi_cd))
print(mi_cd.__str__())

del mi_cd  #ESTO BORRA EL OBJETO mi_cd, no informa, solo elimina
