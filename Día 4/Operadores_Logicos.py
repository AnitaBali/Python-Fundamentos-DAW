#Operador and
mi_bool=4<5 and 5>4
print(mi_bool)
#Se cumplen las dos condiciones, es TRUE

texto="Ana esta en su casa estudiando"
prueba=("casa" in texto.lower()) and ("ana" in texto.lower())
print(prueba)

#Operador or
mi_bool2=10==10 or 3==2
print(mi_bool2)
#Se cumple una de las condicones, es TRUE

#Operador not
otro=not 'a'=='b'
print(otro)
#Imprimirá TRUE. Es como decir a y b no son iguales, el not hace eso, si no es igual será TRUE.