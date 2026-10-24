Saldototal = 1000

def Deposito(num1):
    if num1 < 0:
        print("La cantidad a de ser mayor que 0")
        return Saldototal
    else:
        resultado = num1 + Saldototal
        return resultado

def retiro(num1):
    if  num1 > Saldototal:
        print("No puede retirar mas dinero del que tiene")
        return Saldototal
    else:
        resultado = Saldototal - num1
        return resultado


def menu():
    print(
"""
*** MENU ***
1. Consultar dinero
2. Depositar dinero
3. Retirar dinero
0. Salir.
""")

def leerOpcion():
    opcion = input(">>>Opcion? ")
    while opcion < "0" or opcion > "3":
        print("--> Error. Opción no válida.")
        input("Presione enter para continuar ....")
        print("\n\n\n\n\n")
        menu()
        opcion = input(">>>Opcion? ")

    return int(opcion)

def ConsultarSaldo():
    print("\n\n\n 1. Consultar el saldo")

    print("Su saldo es de: ", Saldototal)

def Depositar():
    print("\n\n\n 2. Depositar dinero")

    depositacion = int(input("\nIngrese la cantidad a depositar "))
    print("\nNuevo saldo: ", Deposito(depositacion))
    return Deposito(depositacion)

def Retirar():
    print("\n\n\n 3. Retirar Dinero")

    retiracion = int(input("\nIngrese la cantidad a retirar "))
    print("\nNuevo saldo: ", retiro(retiracion))
    return retiro(retiracion)
    

### Programa principal
while True:
    menu()
    opcion = leerOpcion()
    match opcion:
        case 1:
            ConsultarSaldo()
        case 2:
            Saldototal = Depositar()
        case 3:
            Saldototal = Retirar()
        case 0:
            print("Gracias por usar la calculadora...")
            break

    input("Presione Enter para continuar...")