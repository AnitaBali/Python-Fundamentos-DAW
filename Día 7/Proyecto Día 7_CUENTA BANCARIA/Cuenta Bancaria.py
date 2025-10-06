from os import system

# CREAR CLASE PERSONA, DOS ATRIBUTOS: NOMBRE Y APELLIDO
class Persona:

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

# CREAR CLASE CLIENTE, HEREDA DE PERSONA. ATRIBUTOS PROPIOS: NUMERO CUENTA Y BALANCE(SALDO)
# MÉTODOS CLASE CLIENTE: TRES
     # METODO ESPECIAL PARA IMPRIMIR A NUESTRO CLIENTE, CUANDO SE IMPRIMA MOSTRARA TODOS LOS DATOS DEL CLIENTE
     # METODO DEPOSITAR, PARA AGREGAR DINERO EN CUENTA
     # METODO RETIRAR , PARA RETIRAR DINERO DE LA CUENTA
class Cliente(Persona):
    def __init__(self,nombre, apellido, numero_cuenta,balance=0):
        super().__init__(nombre,apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} \nNúmero Cuenta: {self.numero_cuenta} \nSaldo: {self.balance} euros"

    def depositar(self,cantidad_dinero):
        if cantidad_dinero<0:
            print("Tienes que ingresar más de 0 euros.")
        else:
            self.balance+=cantidad_dinero
            print(f"Ingresaste {cantidad_dinero} euros. ")

    def retirar(self, cantidad_dinero):
        if cantidad_dinero>self.balance:
            print("Fondos insuficientes.")
        else:
            print(f"Retiraste {cantidad_dinero} euros.")
            self.balance-=cantidad_dinero


# PROGRAMA PIDE AL USUARIO HACER DEPOSITOS O RETIROS. HACE LOOP HASTA QUE USUARIO DECIDA SALIR
# CREAR FUNCIONES APARTE:
       # CREAR CLIENTE PIDIENDO INFORMACIÓN NECESARIA CON UN RETURN DE CLIENTE CREADO
       # CREAR MENU CON OPCIONES, LA PRIMERA SERIA CREAR AL CLIENTE Y LUEGO YA PEDIR QUE INGRESE O RETIRE
def crear_cliente():
    nombre_cl=input("Nombre: ")
    apellido_cl=input("Apellido: ")
    numero_cuenta=input("Ingrese su número de cuenta: ")
    system('cls')

    cliente=Cliente(nombre_cl,apellido_cl,numero_cuenta)
    return cliente

def inicio():
    mi_cliente=crear_cliente()
    print(mi_cliente)
    opcion=0

    while opcion !='S':
        print("Elije: Depositar (D), Retirar (R) o Salir (S)")
        opcion=input()

        if opcion=='D':
            deposito=int(input("Cantidad a depositar: "))
            mi_cliente.depositar(deposito)
        elif opcion=='R':
            retiro = int(input("Cantidad a retirar: "))
            mi_cliente.retirar(retiro)
        print(mi_cliente)

    print("Gracias por operar en Banco Python.")



inicio()







