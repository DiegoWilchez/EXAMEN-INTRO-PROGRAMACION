"""
Objetivo:
Simular un sistema de cajero automático que permita al usuario realizar operaciones básicas como consultar saldo, retirar dinero, depositar dinero y salir. 
Todo debe hacerse mediante el uso de funciones, condicionales y repetitivas.


Requisitos:
1.El programa inicia con un saldo inicial de $1000.
2.Mostrar un menú con las siguientes opciones:
    A.Consultar saldo
    B.Depositar dinero
    C.Retirar dinero
    D.Salir

3.El menú debe repetirse hasta que el usuario seleccione "Salir" o 0 (Cero).
4.Utilizar funciones separadas para cada operación (ConsultarSaldo(), Depositar(), Retirar()).
5.Validar lo siguiente:
    -Que el monto a depositar o retirar sea mayor que cero.
    -Que no se pueda retirar más dinero del disponible.


1.Utilizar condicionales dentro de las funciones para realizar validaciones.
2.Mostrar mensajes claros para el usuario en cada operación.


Pistas para los estudiantes:
-Usar una variable saldo global que se actualice en cada operación.
-Las funciones pueden recibir parámetros si es necesario (por ejemplo, el monto a retirar).
-Usar un bucle mientras o repetir...hasta para mantener el programa corriendo hasta que se elija salir.


"""

saldo = 1000

def consultar_saldo(saldo):
    return saldo

def depositar(saldo):
    deposito = int(input("ingrese el valor a depositar"))
    if deposito > 0:
        deposito = deposito + saldo
        print("deposito valido")
        print("saldo nuevo",consultar_saldo(deposito))
    else:
        print("Eror en el deposito")
    return deposito


def retirar(saldo):
    monto_a_retirar = int(input("Escriba el valor a retirar"))
    if monto_a_retirar > 0 and  monto_a_retirar <= saldo:
        saldo = saldo - monto_a_retirar
        print("El monto a retirar es valido")
    else:
        print("El saldo es insificiente, intente otra vez")
    return saldo




def mostrar_menu(saldo):
    while True:
        print("----MENU----")
        print("A.consultar saldo")
        print("B.depositar dinero")
        print("c.retirar dinero")
        print("D.salir")
    
        opcion = input("elije la opcion")
        match opcion:
            case"A":
                print("consultar saldo")
                print("saldo disponible",consultar_saldo(saldo))
            case"B":
                print("depositar saldo")
                saldo = depositar(saldo)
            case"C":
                print("retirar dinero")
                saldo = retirar(saldo)
            case"D":
                print("salir")
                break

mostrar_menu(saldo)