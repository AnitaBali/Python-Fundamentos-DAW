"""
CELSIUS A FAHRENHEIT: celsius*(9/5)+32
FAHRENHEIT A CELSIUS: fahrenheit-32*9/5
"""

def gradosCelsius(dato):
    formula=dato*9/5+32
    print(f"El equivalente de {dato} grados Celsius en Fahrenheit es {formula} grados.")

def gradosFahrenheit(dato):
    formula=(dato-32)*(5/9)
    print(f"El equivalente de {dato} grados Fahrenheit en Celsius es {formula} grados.")


unidad=""
grados=int(input(f"Usuario, ¿ cuantos grados quiere convertir?:  "))

while unidad!='C' and unidad!='F':
    unidad = input("Usuario, dime que unidad quieres convertir, ¿C=Celsius o F=Farhrenheit?: ")
    if unidad=='C':
        gradosCelsius(grados)
        break
    elif unidad=='F':
        gradosFahrenheit(grados)
        break

