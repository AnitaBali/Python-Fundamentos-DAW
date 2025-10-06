import bs4
import requests
import lxml


#Scraping, primero creamos variable con el enlace de nuestra web
resultado= requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")

sopa=bs4.BeautifulSoup(resultado.text, 'lxml')
print(sopa.select("title")[0].getText()) #Buscar etiqueta de titulo, sin los corchetes
#print(sopa.select("h1")) #Buscar etiqueta de h1

parrafo_especial=sopa.select("a")[3].getText() #Extraer un parrafo
print(parrafo_especial)

columna_lateral=sopa.select('.post-header a')

for a in columna_lateral:
    print(a.getText())
#print(columna_lateral)


#print(type(resultado))
#print(resultado.text) #Muestra el codigo de la web con strings






