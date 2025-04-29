from números import *

turno_perfumeria = decorador_turno(generador_perfumeria)
turno_farmacia = decorador_turno(generador_farmacia)
turno_cosmetica = decorador_turno(generador_cosmetica)

def menu():
    print("\nBienvenido")
    print("1. Perfumería")
    print("2. Farmacia")
    print("3. Cosméticos")
    print("4. Salir\n")

def inicio():

    while True:

        menu()

        try:
            opcion = input("Ingrese el número del área al que desee ingresar: ")

            if opcion == "1":
                turno_perfumeria()
            elif opcion == "2":
                turno_farmacia()
            elif opcion == "3":
                turno_cosmetica()
            elif opcion == "4":
                print("Gracias por su visita, vuelva pronto.")
                break
            else:
                print("Ingrese una opcion valida.")

        except ValueError:
            print("Ingrese un número válido.")

inicio()