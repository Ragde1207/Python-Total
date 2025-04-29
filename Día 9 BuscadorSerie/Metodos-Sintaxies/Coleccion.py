'''
Biblioteca integrada de Python:
from collection import *

Collection permite completar y manipular estructuras de datos de forma más eficiente
'''

from collections import Counter, deque
from collections import defaultdict
from collections import namedtuple

#Counter: permite contar caracteres o numeros en una lista
numeros = [2,3,4,2,3,5,6,3,2,4,6,1]
frase = 'Rūru wa yaburu tame ni aru'
frase2 = 'pepe pica papas con un pico pica papas pepe'

print(Counter(numeros))
print(Counter('mississipi'))
print(Counter(frase.split())) #split()
print(Counter(frase2.split()))

serie = Counter([1,1,1,1,2,2,2,3,3,3,3,3,3,4])

#Al crear una lista con un counter, la crea con los elementos unicos del counter
print(list(serie))
#.most_common crea una tupla ordenando los caracteres/numeros del más comun al menos comun
print(serie.most_common())
#.values devuelve solo la cantidad de veces que se repite un  caracter/numero
print(serie.values())

#deque() permite crear listas de doble entrada (al inicio y al final)
lista = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista)

#.appendleft ingresa datos al inicio de la lista
lista.appendleft("México")
print(lista)

#con deque() podemos seguir usando .append() para agregar nuevos datos a la lista de forma normal
lista.append("Veracruz")
print(lista)


print('------')

#defaultdict(lambda: permite crear un contenido de emergencia para casos en los que se solicite una clave no existente
dic = defaultdict(lambda:'Clave no encontrada')

dic['uno'] = 'rojo'

print(dic['ocho'])

print('------')

'''
namedtuple() permite nombrar el orden de los datos de una tupla, o dicho de otra forma, nombra los indices de
una tupla, esto permite utilizar los datos sin necesidad de recordar su posición especifica y llamarlos
en base al nombre asignado con namedtuple()
'''
Persona = namedtuple('Persona',['nombre','edad','altura'])
rabi = Persona('Rabi',22,1.65)

print(rabi.nombre)