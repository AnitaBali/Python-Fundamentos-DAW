#Convertir a lista de tuples dos listas
nombres=['Ana','Borja','Valeria']
edades=[35,37,2]
ciudades=['Lima','Madrid','Mexico']

combinados=list(zip(nombres,edades,ciudades))  #Hay que castear a list
for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

#Imprime: Ana tiene 35 años y vive en Lima
#Borja tiene 37 años y vive en Madrid
#Valeria tiene 2 años y vive en Mexico