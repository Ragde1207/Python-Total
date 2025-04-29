class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return (f"\nEl cliente es: {self.nombre} {self.apellido}\n"
                f"Numero de cuenta: {self.numero_cuenta}\n"
                f"Saldo en cuenta: ${self.balance}")

    def deposito(self, cantidad):
        self.balance += cantidad
        print(f"Depósito exitoso.\n")


    def retiro(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Retiro exitoso.\n")
        else:
            print("Fondos insuficientes.\n")

def crear_cliente():

    nombre_c = input("Ingrese su nombre: ")
    apellido_c = input("Ingrese su apellido: ")
    cuenta_c = input("Ingrese su numero de cuenta: ")
    balance_c = float(input("Ingrese el monto inicial en su cuenta: "))

    persona_cliente = Cliente(nombre_c,apellido_c,cuenta_c,balance_c)

    return persona_cliente

def inicio():

    usuario = crear_cliente()
    continuar = True

    print(f"\n\nBienvenido {usuario.nombre} {usuario.apellido}")

    while continuar:

        print(f"\nMenú:\n"
              f"1. Datos de usuario\n"
              f"2. Deposito\n"
              f"3. Retiro\n"
              f"4. Salir\n")

        decision = input("\nIngrese la accion a realizar (1 al 4): ")

        if decision == "1":
            print(usuario)
        elif decision == "2":
            try:
                dep = float(input("\nIngrese la cantidad a depositar: "))
                usuario.deposito(dep)
            except ValueError:
                print("\nError: Ingrese un número válido")
        elif decision == "3":
            try:
                ret = float(input("\nIngrese la cantidad a retirar: "))
                usuario.retiro(ret)
            except ValueError:
                print("Error: Ingrese un número válido")
        elif decision == "4":
            continuar = False
            print("\nGracias por usar nuestro servicio")
        else:
            print("\nOpción no válida, por favor ingrese un numero del 1 al 4")

inicio()