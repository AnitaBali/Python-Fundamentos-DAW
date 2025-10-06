def reducir_lista(lista):
    eliminar_duplicados=set(lista)
    nueva_lista=list(eliminar_duplicados)
    mayor=max(nueva_lista)
    nueva_lista.remove(mayor)

    return nueva_lista

def promedio(lista):
    contar=0
    suma=0
    for e in lista:
        contar+=1
        suma=suma+e

    print(contar)
    print(suma)
    return suma/contar


lista_numero=[1,2,3,4,1,2,3,4,90,10,1,2,1,2,1,9]

mi_lista=reducir_lista(lista_numero)
print(round(promedio(mi_lista)))
