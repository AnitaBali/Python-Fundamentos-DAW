from random import *

# ADIVINA EL NUMERO
# PASO 1: BIENVENIDA AL USUARIO Y PREGUNTAR SU NOMBRE
print("-----------------BIENVENIDO A ADIVINA EL NÚMERO-----------------")
nombre=input("Usuario, dime tu nombre: ")
print("----------------------------------------------------------------")

#PASO 2: PREGUNTAR NUMERO ENTRE 1 Y EL 100 AL USUARIO
print(f"Bueno, {nombre}, he pensado un número ente 1 y 100, y tienes solo\nocho intentos para "
      f"adivinar cuál crees que es el número.")
print("----------------------------------------------------------------")

#PASO 3: CREAR VARIABLES NÚMERO A ADIVINAR, NÚMERO USUARIO E INTENTOS
numero_adivinar=randint(1,100) #Numero a adivinar
intentos=8
contador=0

while intentos!=0:
    numero_usuario=int(input("Usuario, introduzca un número entre 1-100: "))
    intentos -= 1
    contador += 1
    if numero_usuario>0 and numero_usuario<101:
        if numero_usuario<numero_adivinar:
            print("Respuesta es incorrecta, ha elegido un número menor al número secreto.")
            if intentos==0:
                print("Has perdido. Agotaste los 8 intentos.")
        elif numero_usuario>numero_adivinar:
            print("Respuesta es incorrecta, ha elegido un número mayor al número secreto.")
            if intentos==0:
                print("Has perdido. Agotaste los 8 intentos.")
        else:
            print(f"Ha adivinado el número, has necesitado {contador} intentos.")
            break
        print("----------------------------------------------------------------")

    else:
        print("El número debe estar dentro del rango.")


