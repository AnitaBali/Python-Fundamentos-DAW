import shutil
import os
import re
import time
import datetime
import timeit
from pathlib import Path
import math

inicio=time.time()

#Descomprimir zip
#shutil.unpack_archive('Proyecto+Dia+9.zip','Extracción','zip')


#Ruta donde esta el directorio
ruta='C:\\Users\\LENOVO\\PycharmProjects\\Python\\Día 9\\Proyecto Día 9\\Extracción\\Mi_Gran_Directorio\\'
#Patrón, debe empezar por letra "N" + 3 caracteres no numericos + 5 caracteres numericos
mi_patron=r'N\D{3}-\d{5}'
#Fecha actual al hacer la ejecución
hoy=datetime.date.today()
#Listas que almacenan las listas de series
numeros_encontrados=[]
archivos_encontrados=[]

#Función que busque los números de serie en los archivos
def buscar_numero(archivo,patron):
    este_archivo=open(archivo,'r')
    texto=este_archivo.read()
    if re.search(patron,texto):
        return re.search(patron,texto)
    else:
        return ""

#Crear lista con los números de serie y archivos
def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado=buscar_numero(Path(carpeta,a),mi_patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())

#Mostrar resultados
def mostrar_todo():
    indice=0
    print('-'*50)
    print(f'Fecha de búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print("ARCHIVO\t\t\tNRO. SERIE")
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f"{a}\t {numeros_encontrados[indice]}")
        indice+=1
    print('\n')
    print(f"Números encontrados: {len(numeros_encontrados)}")
    fin=time.time()
    duracion=fin-inicio
    print(f"Duración de la búsqueda: {math.ceil(duracion)} segundos.")
    print('-'*50)

crear_listas()
mostrar_todo()




