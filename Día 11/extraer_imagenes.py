import bs4
import requests

#Esto es para extraer fotos de sitios online

resultado=requests.get("https://www.escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1")

sopa=bs4.BeautifulSoup(resultado.text,'lxml')

imagenes=sopa.select('.ProductImage')[0]['src'] #Clase de la imagen
print(imagenes)

imagen_curso_1=requests.get((imagenes))
#print(imagen_curso_1.content)

f=open('mi_imagen.jpg','wb')
f.write(imagen_curso_1.content)
f.close()