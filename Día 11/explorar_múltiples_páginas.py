import bs4
import requests


#Crear variable url sin número de pagina
url_base="https://books.toscrape.com/catalogue/page-{}.html"

#Lista de títulos con 4 o 5 estrellas
titulos_rating_alto=[]

#Iterar paginas
for pagina in range(1,3):

    #Crear sopa en cada página
    url_pagina=url_base.format(pagina)
    resultado=requests.get(url_pagina)
    sopa=bs4.BeautifulSoup(resultado.text,'lxml')

    #Seleccionar datos de los libros
    libros=sopa.select('.product_pod')

    #Iterar en los libros
    for libro in libros:

        #Chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) !=0 or len(libro.select('.star-rating.Five')) !=0:
            #Guardar titulo en variable
            titulo_libro=libro.select('a')[1]['title']
            #Agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

#Ver los libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)







"""
#Loop para imprimir las paginas del 1 al 11
for n in range(1,11):
    print(url_base.format(n))


#Extraer los titulos de libros con mas de 4 estrellas en las 10 páginas a analizar

resultador=requests.get(url_base.format('1'))
sopa=bs4.BeautifulSoup(resultador.text,'lxml')
#print(len(sopa.select('.product_pod'))) #Número de libros en la página 1

libros=sopa.select('.product_pod')

ejemplo=libros[0].select('a')[1]['title']
print(ejemplo)
"""