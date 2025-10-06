from pathlib import Path

#Devuelve el antecesor
base=Path.home()
guia=Path(base,'Europa','España', Path("Madrid","Cibeles.txt"))

print(guia.parent.parent)