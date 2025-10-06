diccionario={'c1':'valor1','c2':'valor2'}
print(diccionario)


resultado=diccionario['c1']
print(resultado)
#Imprimirá valor1

cliente={'nombre':'Ana','apellido':'Garcia','peso':55,'talla':1.70}
consulta=cliente['apellido']
print(consulta)

dic={'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
#Imprimirá el 20

nuevo={'c1':['a','b','c'],'c2':['d','e','f'] }
modificacion=nuevo['c2'][1].upper()
modificacion2=nuevo['c1'][0].upper()
print(modificacion)
print(modificacion2)

varios={1:'a',2:'b'}
print(varios)
varios[3]='c'
print(varios)

varios[2]='B'
print(varios)

print(varios.keys())
#Imprimira: dict_keys([1, 2, 3])

print(varios.values())
#Imprimira: dict_values(['a', 'B', 'c'])

print(varios.items())
#Imprimira: dict_items([(1, 'a'), (2, 'B'), (3, 'c')])
