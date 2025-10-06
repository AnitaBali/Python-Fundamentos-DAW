from pathlib import Path
import os
from os import system

ruta=Path('C:\\Users\\LENOVO\\OneDrive\\Escritorio\\DAW\\UDEMY\\Recetas')
nombre=""
opcion=0
categorias=['Carnes','Ensaladas','Pastas','Postres']

def contar_recetas(ruta):
    """
    El mé. os.walk() es ideal para recorrer todos los directorios y archivos dentro de una estructura de carpetas.

    """
    contar=0 #Inicio contador a cero
    for (ruta_actual,subrutas,archivos) in os.walk(ruta):   # La función os.walk() recorre la estructura de directorios.
        for archivo in archivos:
            if archivo.endswith('.txt'):  # Para cada archivo, verificamos si su nombre termina con '.txt'.
                contar+=1
    return contar # Devolvemos el total de archivos contados.

def elegir_categoria(lista):
    categoria=input(f"Elige una categoría entre la disponibles: {lista}")
    if categoria in lista:
        print("¿ Qúe receta quieres leer?")
    else:
        print("La categoría no existe.")





total=contar_recetas(ruta)


#Programa Principal y Menú
print("----------------Bienvenido al Recetario de 'Sabores del Mundo'----------------")
nombre=input("Usuario indicame tu nombre: ")
system('cls')
print(f'''
Hola {nombre}, la ruta de acceso al recetario es: {ruta}
Actualmente hay un total de {total} recetas almacenadas.''')

while opcion!="6":
    opcion= input('''Elige una opción númerica entre 1-6:
    - Opción 1--------------------> Leer Receta
    - Opción 2--------------------> Crear Receta
    - Opción 3--------------------> Crear Categoría
    - Opción 4--------------------> Eliminar Receta
    - Opción 5--------------------> Eliminar Categoría
    - Opción 6--------------------> Finalizar Ejecución
    ''')
    system('cls')
    if opcion=="1":
        mostrar_categoria(categorias)
        print("1")
    elif opcion=="2":
        print("2")
    elif opcion=="3":
        print("3")
    elif opcion=="4":
        print("4")
    elif opcion=="5":
        print("5")
    elif opcion=="6":
        print("Saliendo...")
    else:
        print("Opción no válida.")



