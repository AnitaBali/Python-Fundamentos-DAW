precios_cafe=[('capuchino',2.5),('expresso',1.2),('moka',1.9)]

def cafe_caro(lista):
    precio_mayor=0
    cafe_mas_caro=''

    for cafe,precio in lista:
        if precio>precio_mayor:
            precio_mayor=precio
            cafe_mas_caro=cafe
        else:
            pass

    return cafe_mas_caro,precio_mayor

print(cafe_caro(precios_cafe))



