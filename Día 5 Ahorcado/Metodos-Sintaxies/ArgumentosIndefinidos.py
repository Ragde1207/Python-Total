#*args

'''*arg permite definir funciones genericas sin necesidad de  especificar
    el numero de argumentos, en cambio se adaptaran a la cantidad
    de argumentos que el usuario ingresara.

    "arg" no es necesariamente el nombre del metodo, en este caso
    se puede utilizar cualquier palabra (*gato,*n,*sol) siempre
    y cuando vaya despues de un "*", pero de forma general,
    arg es la palabra normalizada para este metodo'''
from traceback import print_tb


def sumarg(*args):

    total = 0

    for arg in args:
        total += arg

    return total

print(sumarg(3,15,6163,2,1,67,7))

print("\n--------------------------------------------------------------\n")

#**kwargs
'''Al igual que con *args, **kwargs permite usar cualquier palabra
    mientras sea despues de los "**", se utiliza para acceder a
    los nombres de los argumentos ingresados al llamar a una
    funcion, y que a su vez, permite acceder a estos mediante
    un diccionario, ya sea para obtener el item completo,
    la clave o su valor'''

def sumakw(**kwargs):
    #Al momento de ser ingresados en un **kwargs, los datos pasan a ser un diccionario
    suma = 0

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        suma += valor
    return suma

print(sumakw(x=3,y=5,z=1))

print("\n--------------------------------------------------------------\n")

#Funcion mezclada:

#El orden de una funcion mezclada es ("valores normales","argumentos *args","argumentos **kwargs")
def suma(n1,n2,*args,**kwargs):

    print(f"El primer valor es: {n1}")
    print(f"El primer valor es: {n2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")

#Estas variables pueden llevar cualquier nombre, se usaron estos para el ejemplo
args = [15,632,1712472,1,42]
kwargs = {"x":"1","y":"2","z":"3"}

suma(15,50,*args,**kwargs)