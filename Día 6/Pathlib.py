from pathlib import Path, PureWindowsPath

#No hace falta ni open ni close para leer
carpeta=Path('C:/Users/LENOVO/PycharmProjects/Python/Día 6/Alternativa/otro.txt')
print(carpeta.read_text())
#Imprime contenido del texto

#Mét. name, que nos devuelve el nombre del archivo
carpeta=Path('C:/Users/LENOVO/PycharmProjects/Python/Día 6/Alternativa/otro.txt')
print(carpeta.name)
#Imprime: otro.txt

#Mét. suffix nos devuelve la extension del archivo
carpeta=Path('C:/Users/LENOVO/PycharmProjects/Python/Día 6/Alternativa/otro.txt')
print(carpeta.suffix)
#Imprime: .txt

#Mét. stem que nos devuelve el nombre del archivo sin la extensión
carpeta=Path('C:/Users/LENOVO/PycharmProjects/Python/Día 6/Alternativa/otro.txt')
print(carpeta.stem)
#Imprime: otro

#Mét. exist que nos devuelve un booleano de si existe o no
carpeta=Path('C:/Users/LENOVO/PycharmProjects/Python/Día 6/Alternativa/otro.txt')
if not carpeta.exists():
    print("No existe")
else:
    print("Existe")

