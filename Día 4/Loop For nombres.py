lista=["Ana","Pablo","Esther","Borja","German","Leo","Lola"]

for nombre in lista:
    if nombre.startswith("L"): #Comprueba si nombre empieza por la letra pasada
        print(nombre)
    else:
        print(f"{nombre} no comienza con L")