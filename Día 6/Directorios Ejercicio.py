from pathlib import Path

carpeta=Path('C:/Users/LENOVO/PycharmProjects/Python/Día 6/Alternativa') / 'otro.txt'

mi_archivo=open(carpeta)
print(mi_archivo.read())