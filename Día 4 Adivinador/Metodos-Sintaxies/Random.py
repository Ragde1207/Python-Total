#El metodo randint permite generar numeros aleatoreos
#Para utilizar el metodo randint, se necesita importarlo a partir de la libreria random
#from random import * (importa todas las funciones de la libreria)
#from random import "" (las "" es donde se especifica el metodo/funcion a importar)
#Un punto importante es no nombrar el archivo .py no debe tener el nombre de la libreria, sino
#no se importaria la libreria que se necesita usar

from random import * #si la linea aparece en gris es porque aun no se utiliza la funcion

azar = randint(1,15) #("rango de inicio","rango maximo")
print(azar)

azar = uniform(1,3) #uniform genera un numero float de entre el rango de creacion
print(azar)

azar = round(azar,3) #Tambien se puede especificar cuantos decimales usar con el metodo round
print(azar)

azar = random() #random genera un numero (int o float) al azar de entre 0 y 1
print(azar)

print("\n--------------------------------------------------------------\n")

lista = ["Rabi","Herta","Maya","Seele"]
azar = choice(lista) #permite elegir un dato al azar de una lista
print(azar)

print("\n--------------------------------------------------------------\n")

numeros = list(range(1,100,10))
print(numeros)
shuffle(numeros) #Ordena de forma aleatorea los datos de una lista, y no es almacenable en una lista
print(numeros)