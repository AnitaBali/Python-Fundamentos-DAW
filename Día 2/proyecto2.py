

print("----Bienvenido----")
nombre=input("Ingrese su nombre: ")
venta=input("¿Cuanto has vendido este mes? ")
total=float(venta)
comision=round(total*13/100,2)

print(f"Hola {nombre}, has recibido unas comisiones de {comision} euros.")