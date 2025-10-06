import os

#print(os.walk("C:\\Users\\LENOVO\\OneDrive\\Escritorio\\Carpeta Superior"))

ruta="C:\\Users\\LENOVO\\OneDrive\\Escritorio\\Carpeta Superior"

for carpeta,subcarpeta,archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}'")
    print("Los archivos son: ")
    for arch in archivo:
        if arch.startswith("2015"):
            print(f"\t{arch}'")
    print("\n")