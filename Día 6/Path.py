from pathlib import Path

base=Path.home()
guia=Path(base,'Barcelona', 'Sagrada Familia.txt')
print(base) #Ruta absoluta
print(guia) #Ruta relativa
#Devuelve base: C:\Users\LENOVO
#Devuelve guia: C:\Users\LENOVO\Barcelona\Sagrada Familia.txt

#Crear rutas alternativas
base=Path.home()
guia=Path(base,'Europa','España', Path("Madrid","Cibeles.txt"))
guia2=guia.with_name('El_Prado.txt')
print(guia)
print(guia2)
#Imprime: C:\Users\LENOVO\Europa\España\Madrid\Cibeles.txt
#ImprimeC:\Users\LENOVO\Europa\España\Madrid\El_Prado.txt