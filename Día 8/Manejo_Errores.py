def suma():
    n1=int(input("Número 1:"))
    n2 = int(input("Número 2:"))
    print(n1+n2)
    print("Gracias por sumar"+n1)

try:
    suma()
except TypeError:
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    print("Estas ingresando un valor no númerico")
else:
    print("Todo OK")
finally:
    print("Fin")


'''try:
    # Código que queremos probar
    suma()
except:
    # Código a ejecutar si hay un error
    print("Algo no ha salido bien")
else:
    # Código a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    # Código a ejecutar de todos modos
    print("Eso fue todo")
'''