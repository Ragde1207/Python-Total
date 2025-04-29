'''Estructura de funciones:
def NombreFuncion():
   Todo el codigo de la funcion va con tabulacion

NombreFuncion() - Forma de llamar a la funcion
'''

def saludito():
    '''
    Funcion para saludar al usuario
    '''
    print("Hola")

saludito()

def saluditoA(nombre):
    '''
    Funcion para saludar al usuario
    '''
    print(f"Hola {nombre}")

saluditoA(input("Cómo te llamas? "))

print("\n-----------------------------------------------------------------------\n")

def multiplicacion(n1,n2):
    return n1 * n2

resultado = multiplicacion(4,16)
print(resultado)